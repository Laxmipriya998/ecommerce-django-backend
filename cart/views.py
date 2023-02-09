from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer
from product.models import Product
from drf_yasg.utils import swagger_auto_schema


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)
   
    @swagger_auto_schema(request_body=CartSerializer)  
    def post(self, request):
        product_id = request.data.get("product")
        quantity = request.data.get("quantity")
        
        if not product_id or not quantity:
            return Response(
                {"error": "Product and quantity required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product = Product.objects.get(id=product_id)

            if product.stock < int(quantity):
                return Response({"error": "Not enough stock"}, status=400)

            cart = Cart.objects.create(
                user=request.user,
                product=product,
                quantity=quantity
            )

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=201)

        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
            if product.stock < quantity:
                return Response({"error": "Not enough stock"}, status=400)