import logging
from django.utils.dateparse import parse_datetime
from src.orders.models import Orders, OrderShippings, OrderProducts
from src.customers.models import Customers
from src.addresses.models import Addresses
from src.logistics.models import Logistics
from src.relationships.models import OrderProductsOrderShippings, OrdersOrderShippings
from src.apiintegrations.services.mapping import MAPPING

def map_fields(api_data, mapping):
    mapped_data = {}

    for api_field, db_field in mapping.items():
        keys = api_field.split(".")
        value = api_data

        try:
            for key in keys:
                if "[" in key and "]" in key:
                    base_key, index = key.split("[")
                    index = int(index.replace("]", ""))
                    value = value.get(base_key, [])[index] if isinstance(value.get(base_key, []), list) else None
                else:
                    value = value.get(key, None)
        except (IndexError, AttributeError):
            value = None

        mapped_data[db_field] = value

    return mapped_data


def create_customer(customer_data):

    customer, _ = Customers.objects.get_or_create(
        integrationcustomerid=customer_data.get('customer_id'),
        defaults={
            'firstname': customer_data.get('firstname', ''),
            'lastname': customer_data.get('lastname', ''),
        }
    )
    return customer


def create_ordershipping(shipping_data):

    logistics, _ = Logistics.objects.get_or_create(
        carriercode=shipping_data.get('shipping_carrier_code'),
        defaults={'title': shipping_data.get('shipping_company', '')}
    )

    return OrderShippings.objects.create(
        shippingprice=shipping_data.get('shipping_price', 0.0),
        estimateddate=parse_datetime(shipping_data.get('shipping_deadline')),
        logistics=logistics,
        tracking=shipping_data.get('shipping_tracking', ''),
        tracking_url=shipping_data.get('shipping_tracking_url', ''),
        zonecode=shipping_data.get('shipping_zone_code', ''),
    )


def create_address(address_data, shipping_instance):

    Addresses.objects.create(
        street_1=address_data.get('street_1', ''),
        street_2=address_data.get('street_2', ''),
        zipcode=address_data.get('zip_code', ''),
        city=address_data.get('city', ''),
        country=address_data.get('country', ''),
        state=address_data.get('state', ''),
        ordershippings=shipping_instance
    )


def create_order(order_data, customer, integration, shipping_instance):

    order_instance, _ = Orders.objects.update_or_create(
        integrationorderid=order_data.get('order_id'),
        defaults={
            'title': order_data.get('commercial_id', ''),
            'integrationstatus': order_data.get('order_state', ''),
            'integrations': integration,
            'currency': order_data.get('currency_iso_code', ''),
            'customers': customer,
            'purchase_date': parse_datetime(order_data.get('created_date')),
            'delivery_date': parse_datetime(order_data.get('delivery_date_latest')),
            'earliestdelivery_date': parse_datetime(order_data.get('delivery_date_earliest')),
            'latestdelivery_date': parse_datetime(order_data.get('delivery_date_latest')),
            'totalprice': float(order_data.get('total_price', 0.0)),
            'totalcomission': float(order_data.get('total_commission', 0.0))
        }
    )

    OrdersOrderShippings.objects.create(
        orders=order_instance,
        ordershippings=shipping_instance
    )

    return order_instance


def create_order_products(products_data, order_instance, shipping_instance, base_url):

    for product in products_data:
        media_url = product.get('product_medias', [{}])[0].get('media_url', '')

        orderproduct = OrderProducts.objects.create(
            title=product.get('product_title', ''),
            sku=product.get('product_sku', ''),
            commission_fee=float(product.get('total_commission', 0.0)),
            price=float(product.get('price_unit', 0.0)),
            quantity=int(product.get('quantity', 0)),
            orders=order_instance,
            shippings=shipping_instance,
            image1=f"{base_url}{media_url}" if media_url else ""
        )

        OrderProductsOrderShippings.objects.create(
            orderproducts=orderproduct,
            ordershippings=shipping_instance,
            receiveddate=parse_datetime(product.get('received_date')) if product.get('received_date') else None
        )