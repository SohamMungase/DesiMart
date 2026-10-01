from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.response import Response

class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

from django.shortcuts import render, get_object_or_404
from products.models import Product
from rest_framework import status

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity') 
        if not product_id:
            return Response({"error": "Product ID is required."})
        product = get_object_or_404(Product, id=product_id, is_active=True)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += int(quantity)
            item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
