from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from rest_framework.response import Response
from .models import Order, OrderItem
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework import status
from .utils import send_order_notification
from rest_framework.generics import ListAPIView, RetrieveAPIView


class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        

        if not cart or cart.items.count() == 0:
            return Response({"error": "Cart is Empty"})

        # create the order

        order = Order.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total,
            status = "CONFIRMED",
            # address = shipping_address.get("address"),
            # phone = shipping_address.get("phone"),
            # city = shipping_address.get("city"),
            # state = shipping_address.get("state"),
            # zip_code = shipping_address.get("zip_code"), 
        )
        # create order items

        cart.items.all().delete()
        cart.delete()
        cart.save()

        # send the response to frontend
        serializer = OrderSerializer(order)
        send_order_notification(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    

