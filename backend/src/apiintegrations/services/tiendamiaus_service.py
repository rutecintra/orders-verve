import logging
from .base_service import BaseIntegrationService
from .database_service import (
    map_fields,
    create_customer,
    create_ordershipping,
    create_address,
    create_order,
    create_order_products
)
from .mapping import MAPPING
from src.integrations.models import Integrations
from src.orders.models import Orders

class TiendamiausService(BaseIntegrationService):
    def __init__(self):
        super().__init__("Tiendamiaus (Mirakl)")

    def get_orders(self):
        orders_data = self.get("orders", params={'paginate': 'false'})
        if not orders_data:
            return

        for order in orders_data.get("orders", []):
            mapped_order = map_fields(order, MAPPING["tiendamiaus"])  # Converte os campos

            existing_order = Orders.objects.filter(integrationorderid=mapped_order["integrationorderid"]).first()
            if existing_order:
                logging.info(f"Pedido {mapped_order['integrationorderid']} já existe no banco. Pulando inserção.")
                continue

            integration = Integrations.objects.get(title="Tiendamiaus (Mirakl)")
            customer = create_customer(map_fields(order.get("customer", {}), MAPPING["tiendamiaus"]))
            shipping_instance = create_ordershipping(map_fields(order, MAPPING["tiendamiaus"]))

            create_address(map_fields(order.get('customer', {}).get('billing_address', {}), MAPPING["tiendamiaus"]), shipping_instance)
            create_address(map_fields(order.get('customer', {}).get('shipping_address', {}), MAPPING["tiendamiaus"]), shipping_instance)

            order_instance = create_order(mapped_order, customer, integration, shipping_instance)

            create_order_products(order.get('order_lines', []), order_instance, shipping_instance, base_url="https://tiendamiaus-prod.mirakl.net/")

            logging.info(f"Pedido {mapped_order['integrationorderid']} salvo com sucesso!")