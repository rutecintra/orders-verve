import logging
from django.utils.dateparse import parse_datetime
from src.orders.models import Orders, OrderShippings, OrderProducts
from src.customers.models import Customers
from src.addresses.models import Addresses
from src.logistics.models import Logistics
from src.relationships.models import OrderProductsOrderShippings, OrdersOrderShippings


def create_customer(customer_data):
    customer, _ = Customers.objects.get_or_create(
        integrationcustomerid=customer_data.get('integrationcustomerid'),
        defaults={
            'firstname': customer_data.get('firstname', ''),
            'lastname': customer_data.get('lastname', ''),
        }
    )
    return customer


def create_ordershipping(shipping_data):
    logistics, _ = Logistics.objects.get_or_create(
        carriercode=shipping_data.get('carriercode'),
        defaults={'title': shipping_data.get('title', '')}
    )

    estimated_date = parse_datetime(shipping_data.get('estimateddate')) if isinstance(shipping_data.get('estimateddate'), str) else None

    return OrderShippings.objects.create(
        shippingprice=shipping_data.get('shippingprice', 0.0),
        estimateddate=estimated_date,
        logistics=logistics,
        tracking=shipping_data.get('tracking', ''),
        tracking_url=shipping_data.get('tracking_url', ''),
        zonecode=shipping_data.get('zonecode', ''),
    )


def create_address(address_data, shipping_instance):
    Addresses.objects.create(
        street_1=address_data.get('street_1', ''),
        street_2=address_data.get('street_2', ''),
        zipcode=address_data.get('zipcode', ''),
        city=address_data.get('city', ''),
        country=address_data.get('country', ''),
        state=address_data.get('state', ''),
        ordershippings=shipping_instance
    )


def create_order(order_data, customer, integration, shipping_instance):
    order_instance, _ = Orders.objects.update_or_create(
        integrationorderid=order_data.get('integrationorderid'),
        defaults={
            'title': order_data.get('title', ''),
            'integrationstatus': order_data.get('integrationstatus', ''),
            'integrations': integration,
            'currency': order_data.get('currency', ''),
            'customers': customer,
            'purchase_date': parse_datetime(order_data.get('purchase_date')),
            'delivery_date': parse_datetime(order_data.get('latestdelivery_date')),
            'earliestdelivery_date': parse_datetime(order_data.get('earliestdelivery_date')),
            'latestdelivery_date': parse_datetime(order_data.get('latestdelivery_date')),
            'totalprice': float(order_data.get('totalprice', 0.0)),
            'totalcomission': float(order_data.get('totalcomission', 0.0)),
        }
    )

    OrdersOrderShippings.objects.create(
        orders=order_instance,
        ordershippings=shipping_instance
    )

    return order_instance


def create_order_products(products_data, order_instance, shipping_instance, base_url):
    for product in products_data:
        orderproduct = OrderProducts.objects.create(
            title=product.get('title', ''),
            sku=product.get('sku', ''),
            commission_fee=float(product.get('totalcomission', 0.0)),
            price=float(product.get('price', 0.0)),
            quantity=int(product.get('quantity', 0)),
            orders=order_instance,
            shippings=shipping_instance,
            image1=f"{base_url}{product.get('image1', '')}" if product.get('image1') else ""
        )

        OrderProductsOrderShippings.objects.create(
            orderproducts=orderproduct,
            ordershippings=shipping_instance,
            receiveddate=parse_datetime(product.get('received_date')) if product.get('received_date') else None
        )
