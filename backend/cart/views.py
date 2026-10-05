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
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")

        if not product_id:
            return Response(
                {"error": "Product ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not quantity:
            return Response(
                {"error": "Quantity is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        quantity = int(quantity)

        if quantity <= 0:
            return Response(
                {"error": "Quantity must be greater than 0."},
                status=status.HTTP_400_BAD_REQUEST
            )

        product = get_object_or_404(
            Product,
            id=product_id,
            is_active=True
        )

        cart, _ = Cart.objects.get_or_create(
            user=request.user
        )

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        # Check total quantity including existing cart quantity
        new_quantity = quantity if created else item.quantity + quantity

        if new_quantity > product.stock:
            return Response(
                {
                    "error": "Not enough stock.",
                    "available_stock": product.stock,
                    "requested_quantity": new_quantity
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        item.quantity = new_quantity
        item.save()

        serializer = CartSerializer(cart)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
class ManageCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, item_id):
        if "change" not in request.data:
            return Response({"error": "change value is required"},status=status.HTTP_400_BAD_REQUEST,)

        change = int(request.data.get("change"))
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        product = item.product

        if change > 0:
            if item.quantity + change > product.stock:
                return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)

        new_qty = item.quantity + change

        if new_qty <= 0:
            item.delete()
            return Response({"success": "Item removed"}, status=status.HTTP_200_OK)

        item.quantity = new_qty
        item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, item_id):
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def delete(self, request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart_user=request.user)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
