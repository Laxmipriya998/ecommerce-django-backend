from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from cart.models import Cart
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order

class PaymentView(APIView):

    def post(self, request):
        order_id = request.data.get("order_id")

        try:
            order = Order.objects.get(id=order_id)
            order.is_paid = True
            order.save()
            return Response({"message": "Payment successful"})
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)
        
class OrderCreateSerializer(serializers.Serializer):
    pass  # no input needed, order is created from cart


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=OrderCreateSerializer)  # 👈 ADD THIS
    def post(self, request):
        cart_items = Cart.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        total_price = 0

        for item in cart_items:
            total_price += item.product.price * item.quantity

        order = Order.objects.create(
            user=request.user,
            total_price=total_price
        )

        cart_items.delete()

        return Response({
            "message": "Order created",
            "total_price": total_price
        }, status=201)
        
        if not order.is_paid:
            return Response({"error": "Payment required"}, status=400)