from django.urls import path
from .views import ProductListCreate

urlpatterns = [
    path('', ProductListCreate.as_view()),
]