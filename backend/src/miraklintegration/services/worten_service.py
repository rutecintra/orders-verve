import logging
from .base_service import BaseIntegrationService
from .database_service import (
    create_customer,
    create_ordershipping,
    create_address,
    create_order,
    create_order_products
)
from .mapping import MAPPING, map_fields
from src.integrations.models import Integrations
from src.orders.models import Orders


class WortenService(BaseIntegrationService):
    def __init__(self):
        super().__init__("Worten (Mirakl)")
        self.integration = Integrations.objects.get(title="Worten (Mirakl)")

    def get_orders(self):
        orders_data = self.get("orders", params={'paginate': 'false'})
        if not orders_data:
            logging.warning("No order returned for Worten API.")
            return

        for order in orders_data.get("orders", []):
            try:
                mapped_order = map_fields(order, MAPPING["worten"])

                if Orders.objects.filter(integrationorderid=mapped_order["integrationorderid"]).exists():
                    logging.info(f"Order {mapped_order['integrationorderid']} already exists. Skipping insertion.")
                    continue

                mapped_customer = map_fields(order.get("customer", {}), MAPPING["worten"])
                customer = create_customer(mapped_customer)

                mapped_shipping = map_fields(order, MAPPING["worten"])
                shipping_instance = create_ordershipping(mapped_shipping)

                mapped_billing_address = map_fields(order.get('customer', {}).get('billing_address', {}), MAPPING["worten"])
                mapped_shipping_address = map_fields(order.get('customer', {}).get('shipping_address', {}), MAPPING["worten"])
                create_address(mapped_billing_address, shipping_instance)
                create_address(mapped_shipping_address, shipping_instance)

                order_instance = create_order(
                    mapped_order,
                    customer,
                    self.integration,
                    shipping_instance
                )

                # mapped_order_lines = [map_fields(product, MAPPING["worten"]) for product in order.get('order_lines', [])]

                for product in order.get('order_lines', []):
                    mapped_product = map_fields(product, MAPPING["worten"])
                    create_order_products(
                        [mapped_product],
                        order_instance,
                        shipping_instance,
                        base_url="https://marketplace.worten.pt/"
                    )

                logging.info(f"Order {mapped_order['integrationorderid']} saved successfully!")

            except Exception as e:
                logging.error(f"Error processing order {order.get('order_id')}: {e}")