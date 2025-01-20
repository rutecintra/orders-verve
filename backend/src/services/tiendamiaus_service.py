import requests
import logging
from django.utils.dateparse import parse_datetime
from src.models.orders import Orders
from src.models.customers import Customers
from src.models.addresses import Addresses
from src.models.integrations import Integrations
from src.models.ordershippings import OrderShippings
from src.models.logistics import Logistics
from src.models.orderproducts import OrderProducts
from src.models.relationships import OrderProductsOrderShippings
from src.models.productimages import ProductImages
from src.models.relationships import OrdersOrderShippings

API_URL = "https://tiendamiaus-prod.mirakl.net/api/orders"
API_KEY = "4745391d-0b7c-4db6-b75c-c1731af15c60"

def process_customer(customer_data):
    return Customers.objects.get_or_create(
        integrationcustomerid=customer_data.get('customer_id'),
        defaults={
            'firstname': customer_data.get('firstname', ''),
            'lastname': customer_data.get('lastname', ''),
        }
    )[0]

def process_order(order, customer, integration):
    return Orders.objects.update_or_create(
        integrationorderid=order.get('order_id'),
        defaults={
            'title': order.get('commercial_id', ''),
            'integration': integration,
            'customer': customer,
            'currency': order.get('currency_iso_code', ''),
            'purchase_date': parse_datetime(order.get('created_date')),
        }
    )[0]


def fetch_orders_from_api():
    headers = {
        'Authorization': API_KEY
    }

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()

        orders_data = response.json().get('orders', [])

        for order in orders_data:

            api_orderid = order.get('order_id')

            existing_order = Orders.objects.filter(integrationorderid = api_orderid).first()

            if existing_order:
                logging.info(f"Pedido {api_orderid} já existe no banco. Pulando inserção.")
                continue

            integration = get_integration()

            customer = process_customer(order.get('customer', {}))

            shipping_data = process_ordershipping(order)

            process_addresses(order.get('customer', {}).get('billing_address', {}), shipping_data)
            process_addresses(order.get('customer', {}).get('shipping_address', {}), shipping_data)

            order_instance = create_order(order, customer, integration, shipping_data)

            process_order_products(order.get('order_lines', []), order_instance, shipping_data)

            logging.info(f"Pedido {api_orderid} salvo com sucesso!")

            # integration = Integrations.objects.get(title = 'Tiendamiaus (Mirakl)')
            
            # customer_data = order.get('customer', {})
            # customer, created = Customers.objects.get_or_create(
            #     integrationcustomerid=customer_data.get('customer_id'),
            #     defaults = {
            #         'firstname': customer_data.get('firstname', ''),
            #         'lastname': customer_data.get('lastname', ''),
            #     }
            # )

            # logistics, created = Logistics.objects.get_or_create(
            #     carriercode = order.get('shipping_carrier_code'),
            #     defaults = {
            #         'title': order.get('shipping_company', 'shipping_carrier_code')
            #     }
            # )

            # shipping_data = OrderShippings.objects.create(
            #     shippingprice = order.get('shipping_price'),
            #     estimateddate = parse_datetime(order.get('shipping_deadline')),
            #     logistics = logistics,
            #     tracking = order.get('shipping_tracking', ''),
            #     tracking_url = order.get('shipping_tracking_url', ''),
            #     zonecode = order.get('shipping_zone_code', ''),
            # )

            # billing_address_data = order.get('billing_address', {})
            # Addresses.objects.create(
            #     street_1 = billing_address_data.get('street_1', ''),
            #     street_2 = billing_address_data.get('street_2', ''),
            #     zipcode = billing_address_data.get('zip_code'),
            #     city = billing_address_data.get('city'),
            #     country = billing_address_data.get('country'),
            #     state = billing_address_data.get('state'),
            #     ordershippings = shipping_data
            # )

            # shipping_address_data = order.get('shipping_address', {})
            # Addresses.objects.create(
            #     street_1 = shipping_address_data.get('street_1', ''),
            #     street_2 = shipping_address_data.get('street_2', ''),
            #     zipcode = shipping_address_data.get('zip_code'),
            #     city = shipping_address_data.get('city'),
            #     country = shipping_address_data.get('country'),
            #     state = shipping_address_data.get('state')
            # )

            # order_data = Orders.objects.update_or_create(
            #     integrationorderid = order.get('order_id'),
            #     defaults={
            #         'title': order.get('commercial_id', ''),
            #         'integrationstatus': order.get('order_state'),
            #         'integrationorderid': order.get('order_id'),
            #         'integrations_id': integration,
            #         'currency': order.get('currency_iso_code', ''),
            #         'customer_id': customer,
            #         'purchase_date': parse_datetime(order.get('created_date')),
            #         'delivery_date': parse_datetime(order['delivery_date'].get('latest')),
            #         'earliestdelivery_date': parse_datetime(order['delivery_date'].get('earliest')),
            #         'latestdelivery_date': parse_datetime(order['delivery_date'].get('latest')),
            #         'totalprice': float(order.get('total_price', None)),
            #         'totalcomission': float(order.get('total_commission', None))
            #     }
            # )

            # products_data = order.get('order_lines', {})
            # orderproduct = OrderProducts.objects.create(
            #     title = products_data.get('product_title'),
            #     integrationorderid = products_data.get('product_shop_sku'),
            #     sku = products_data.get('product_sku'),
            #     commission_fee = products_data.get('total_commission'),
            #     price = float(products_data.get('price_unit')),
            #     quantity = products_data.get('quantity'),
            #     orders = order_data,
            #     shippings = shipping_data
            # )

            # OrderProductsOrderShippings.objects.create(
            #     orderproducts = orderproduct,
            #     ordershippings = shipping_data,
            #     receiveddate = products_data.get('received_date')
            # )

            # OrdersOrderShippings.objects.create(
            #     orders = order_data,
            #     ordershippings = shipping_data
            # )

            # OrdersOrderShippings.objects.create(
            #     orders = order_data,
            #     ordershippings = shipping_data
            # )

            # print(f"Pedido {order.get('commercial_id')} salvo com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar pedidos: {e}")


def get_integration():

    return Integrations.objects.get(title='Tiendamiaus (Mirakl)')


def process_customer(customer_data):
    customer, created = Customers.objects.get_or_create(
        integrationcustomerid = customer_data.get('customer_id'),
        defaults={
            'firstname': customer_data.get('firstname', ''),
            'lastname': customer_data.get('lastname', ''),
        }
    )
    return customer


def process_ordershipping(order):
    logistics, _ = Logistics.objects.get_or_create(
        carriercode = order.get('shipping_carrier_code'),
        defaults = {'title': order.get('shipping_company', 'shipping_carrier_code')}
    )

    shipping_data = OrderShippings.objects.create(
        shippingprice = order.get('shipping_price', 0.0),
        estimateddate = parse_datetime(order.get('shipping_deadline')),
        logistics = logistics,
        tracking = order.get('shipping_tracking', ''),
        tracking_url = order.get('shipping_tracking_url', ''),
        zonecode = order.get('shipping_zone_code', ''),
    )
    return shipping_data


def process_addresses(address_data, shipping_data):
    Addresses.objects.create(
        street_1=address_data.get('street_1', ''),
        street_2=address_data.get('street_2', ''),
        zipcode=address_data.get('zip_code', ''),
        city=address_data.get('city', ''),
        country=address_data.get('country', ''),
        state=address_data.get('state', ''),
        ordershippings=shipping_data
    )


def create_order(order, customer, integration, shipping_data):
    order_instance, created = Orders.objects.update_or_create(
        integrationorderid=order.get('order_id'),
        defaults={
            'title': order.get('commercial_id', ''),
            'integrationstatus': order.get('order_state', ''),
            'integrations': integration,
            'currency': order.get('currency_iso_code', ''),
            'customers': customer,
            'purchase_date': parse_datetime(order.get('created_date')),
            'delivery_date': parse_datetime(order['delivery_date'].get('latest')),
            'earliestdelivery_date': parse_datetime(order['delivery_date'].get('earliest')),
            'latestdelivery_date': parse_datetime(order['delivery_date'].get('latest')),
            'totalprice': float(order.get('total_price', 0.0)),
            'totalcomission': float(order.get('total_commission', 0.0))
        }
    )

    OrdersOrderShippings.objects.create(
        orders = order_instance,
        ordershippings = shipping_data
    )

    return order_instance


def process_order_products(products_data, order_instance, shipping_data):

    base_url = "https://tiendamiaus-prod.mirakl.net/"

    for product in products_data:

        media_url = product.get('product_medias', [{}])[0].get('media_url', '')

        orderproduct = OrderProducts.objects.create(
            title=product.get('product_title', ''),
            sku=product.get('product_sku', ''),
            commission_fee=float(product.get('total_commission', 0.0)),
            price=float(product.get('price_unit', 0.0)),
            quantity=int(product.get('quantity', 0)),
            orders=order_instance,
            shippings=shipping_data,
            image1=f"{base_url}{media_url}" if media_url else ""
        )

        OrderProductsOrderShippings.objects.create(
            orderproducts=orderproduct,
            ordershippings=shipping_data,
            receiveddate=parse_datetime(product.get('received_date')) if product.get('received_date') else None
        )

