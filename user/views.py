from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from drf_yasg.utils import swagger_auto_schema

class RegisterView(APIView):
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"})
        return Response(serializer.errors)