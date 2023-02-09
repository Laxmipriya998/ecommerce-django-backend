from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema 
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


class ProductListCreate(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        products = Product.objects.all()
        
        if not products.exists():
            return Response(
                {"message": "No products found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)