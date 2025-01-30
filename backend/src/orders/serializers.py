from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from .models import Orders, OrderProducts, OrderShippings
from src.relationships.models import OrderProductsOrderShippings, OrdersOrderShippings

class OrderProductsSerializer(serializers.ModelSerializer):
    shippings = serializers.SerializerMethodField()

    class Meta:
        model = OrderProducts
        fields = '__all__'

    def get_shippings(self, obj):
        related_shippings = OrderProductsOrderShippings.objects.filter(orderproducts=obj)
        return OrderProductsOrderShippingsSerializer(related_shippings, many=True).data

class OrderShippingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderShippings
        fields = '__all__'

class OrderProductsOrderShippingsSerializer(serializers.ModelSerializer):
    ordershippings = OrderShippingsSerializer()

    class Meta:
        model = OrderProductsOrderShippings
        fields = ['ordershippings', 'receiveddate', 'shipped_date']

class OrdersSerializer(serializers.ModelSerializer):
    orderproducts = OrderProductsSerializer(many=True, read_only=True)
    ordershippings = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = '__all__'

    @swagger_serializer_method(serializer_or_field=OrderShippingsSerializer(many=True))
    def get_ordershippings(self, obj):
        related_shippings = OrderShippings.objects.filter(
            id__in=OrdersOrderShippings.objects.filter(orders=obj).values_list("ordershippings", flat=True)
        )
        return OrderShippingsSerializer(related_shippings, many=True).data
