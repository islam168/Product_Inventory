from rest_framework import generics
from .models import Enterprise, Category, Product
from .serializers import (EnterpriseListSerializer, EnterpriseSerializer, CategorySerializer,
                          ProductSerializer, ProductListSerializer)
from .services import LargePagination


# Enterprise
class EnterpriseListAPIView(generics.ListAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseListSerializer


class EnterpriseCreateAPIView(generics.CreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class EnterpriseUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


# Category
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LargePagination  # 10 записей на одной странице, в то время как на других страницах по 5


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
