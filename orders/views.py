from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status

from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer
from .utils import send_order_notification


class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        # Get user's cart
        cart = get_object_or_404(
            Cart,
            user=request.user
        )

        # Check if cart is empty
        if cart.items.count() == 0:
            return Response(
                {
                    "error": "Cart is Empty"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get shipping address
        shipping_address = request.data.get(
            "shippingAddress",
            {}
        )

        # --------------------------------
        # Check product stock
        # --------------------------------

        for item in cart.items.all():

            product = item.product

            if product.stock < item.quantity:
                return Response(
                    {
                        "details": (
                            f"Only {product.stock} is left "
                            f"for {product.name}"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        # --------------------------------
        # Create Order
        # --------------------------------

        order = Order.objects.create(
            user=request.user,
            subtotal=cart.subtotal,
            tax_amount=cart.tax_amount,
            grand_total=cart.grand_total,
            status="CONFIRMED",

            # Uncomment if these fields
            # exist in your Order model

            # address=shipping_address.get("address"),
            # phone=shipping_address.get("phone"),
            # city=shipping_address.get("city"),
            # state=shipping_address.get("state"),
            # zip_code=shipping_address.get("zip_code"),
        )

        # --------------------------------
        # Create Order Items
        # --------------------------------

        for item in cart.items.all():

            product = item.product

            # Calculate total price
            total_price = product.price * item.quantity

            # Create OrderItem
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                price=product.price,
                total_price=total_price,
            )

            # --------------------------------
            # Decrease Product Stock
            # --------------------------------

            product.stock -= item.quantity
            product.save()

        # --------------------------------
        # Delete Cart
        # --------------------------------

        cart.items.all().delete()
        cart.delete()

        # --------------------------------
        # Send Order Notification
        # --------------------------------

        send_order_notification(order)

        # --------------------------------
        # Send Response
        # --------------------------------

        serializer = OrderSerializer(order)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class OrderListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        ).order_by("-created_at")


class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )