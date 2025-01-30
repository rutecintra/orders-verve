MAPPING = {
    "tiendamiaus": {
        # Order fields
        "order_id": "integrationorderid",
        "commercial_id": "title",
        "order_state": "integrationstatus",
        "currency_iso_code": "currency",
        "created_date": "purchase_date",
        "delivery_date.latest": "latestdelivery_date",
        "delivery_date.earliest": "earliestdelivery_date",
        "total_price": "totalprice",
        "total_commission": "totalcomission",

        # Customer fields
        "customer.customer_id": "integrationcustomerid",
        "customer.firstname": "firstname",
        "customer.lastname": "lastname",

        # Shipping fields
        "shipping_carrier_code": "carriercode",
        "shipping_tracking": "tracking",
        "shipping_tracking_url": "tracking_url",
        "shipping_price": "shippingprice",

        # Order Products fields
        "order_lines.product_sku": "sku",
        "order_lines.price_unit": "price",
        "order_lines.quantity": "quantity",
        "order_lines.product_medias[0].media_url": "image1",
    },
    "worten": {
        # Order fields
        "id": "integrationorderid",
        "reference": "title",
        "status": "integrationstatus",
        "currency": "currency",
        "created_at": "purchase_date",
        "expected_delivery.max": "latestdelivery_date",
        "expected_delivery.min": "earliestdelivery_date",
        "total_amount": "totalprice",
        "commission_fee": "totalcomission",

        # Customer fields
        "buyer.id": "integrationcustomerid",
        "buyer.name": "firstname",
        "buyer.surname": "lastname",

        # Shipping fields
        "carrier": "carriercode",
        "tracking_number": "tracking",
        "tracking_link": "tracking_url",
        "shipping_cost": "shippingprice",

        # Order Products fields
        "items.sku": "sku",
        "items.unit_price": "price",
        "items.quantity": "quantity",
        "items.images[0].url": "image1",
    }
}


def map_fields(api_data, mapping):
    mapped_data = {}

    for api_field, db_field in mapping.items():
        keys = api_field.split(".")
        value = api_data

        try:
            for key in keys:
                if "[]" in key:
                    key = key.replace("[]", "")
                    value = [map_fields(item, {api_field.replace("[]", ""): db_field}) for item in value.get(key, [])]
                elif "[" in key and "]" in key:
                    base_key, index = key.split("[")
                    index = int(index.replace("]", ""))
                    value = value.get(base_key, [])[index] if isinstance(value.get(base_key, []), list) else None
                else:
                    value = value.get(key, None)

            if isinstance(value, type(None)):
                if "price" in db_field or "commission" in db_field or "quantity" in db_field:
                    value = 0.0

        except (IndexError, AttributeError, ValueError):
            value = 0.0

        mapped_data[db_field] = value

    return mapped_data
