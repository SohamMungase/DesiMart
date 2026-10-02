from decimal import Decimal
from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")

    price = serializers.DecimalField(
        source="product.price",
        max_digits=10,
        decimal_places=2
    )

    tax_percent = serializers.DecimalField(
        source="product.tax_percentage",
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    subtotal = serializers.SerializerMethodField()
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = "__all__"

    def get_subtotal(self, obj):
        subtotal = Decimal("0.00")

        for item in obj.items.all():
            subtotal += item.product.price * item.quantity

        return subtotal

    def get_grand_total(self, obj):
        grand_total = Decimal("0.00")

        for item in obj.items.all():
            item_total = item.product.price * item.quantity

            tax_amount = (
                item_total *
                item.product.tax_percentage /
                Decimal("100")
            )

            grand_total += item_total + tax_amount

        return grand_total