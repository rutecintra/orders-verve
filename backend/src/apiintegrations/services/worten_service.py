import logging
from .base_service import BaseIntegrationService
from .database_service import (
    create_customer,
    create_ordershipping,
    create_address,
    create_order,
    create_order_products
)
from .mapping import MAPPING
from src.integrations.models import Integrations

class WortenService(BaseIntegrationService):
    def __init__(self):
        super().__init__("Worten (Mirakl)")

    def get_orders(self):
        orders_data = self.get("orders")
        if not orders_data:
            return

        for order in orders_data.get("orders", []):
            mapped_order = map_fields(order, MAPPING["worten"])  # Converte os campos

            existing_order = Orders.objects.filter(integrationorderid=mapped_order["integrationorderid"]).first()
            if existing_order:
                logging.info(f"Pedido {mapped_order['integrationorderid']} já existe no banco. Pulando inserção.")
                continue

            integration = Integrations.objects.get(title="Worten (Mirakl)")
            customer = create_customer(map_fields(order.get("buyer", {}), MAPPING["worten"]))
            shipping_instance = create_ordershipping(map_fields(order, MAPPING["worten"]))

            create_address(map_fields(order.get('buyer', {}).get('billing_address', {}), MAPPING["worten"]), shipping_instance)
            create_address(map_fields(order.get('buyer', {}).get('shipping_address', {}), MAPPING["worten"]), shipping_instance)

            order_instance = create_order(mapped_order, customer, integration, shipping_instance)

            create_order_products(order.get('items', []), order_instance, shipping_instance, base_url="https://worten-api-url.com/")

            logging.info(f"Pedido {mapped_order['integrationorderid']} salvo com sucesso!")