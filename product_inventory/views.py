from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Enterprise, Category, Product
from .serializers import (EnterpriseListSerializer, EnterpriseSerializer, CategorySerializer,
                          ProductSerializer, ProductListSerializer)
from .services import LargePagination


# Enterprise
@extend_schema(
    tags=["Enterprise"],  # Tags for API documentation.
    summary="Get a list of enterprises",  # Summary description for the endpoint.
    responses={200: EnterpriseListSerializer},  # Expected response schema.
)
class EnterpriseListAPIView(ListAPIView):
    queryset = Enterprise.objects.all().order_by('id')
    serializer_class = EnterpriseListSerializer


@extend_schema(
    tags=["Enterprise"],
    request=EnterpriseSerializer,
    summary="Create an enterprise",
    responses={200: EnterpriseSerializer},
)
class EnterpriseCreateAPIView(CreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class EnterpriseUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

    @extend_schema(
        tags=['Enterprise'],
        summary="Retrieve enterprise details",
        responses={200: EnterpriseSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=['Enterprise'],
        request=EnterpriseSerializer,
        summary="Update enterprise details",
        responses={200: EnterpriseSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Enterprise'],
        request=EnterpriseSerializer,
        summary="Partially update enterprise details",
        responses={200: EnterpriseSerializer},
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=['Enterprise'],
        summary="Delete enterprise",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Category
@extend_schema(
    tags=["Category"],
    summary="Get a list of categories",
    responses={200: CategorySerializer},
)
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    pagination_class = LargePagination


@extend_schema(
    tags=["Category"],
    request=CategorySerializer,
    summary="Create a category",
    responses={200: CategorySerializer},
)
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(
        tags=['Category'],
        summary="Retrieve category details",
        responses={200: CategorySerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        request=CategorySerializer,
        summary="Update category details",
        responses={200: CategorySerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        request=CategorySerializer,
        summary="Partially update category details",
        responses={200: CategorySerializer},
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        summary="Delete category",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Product
@extend_schema(
    tags=["Product"],
    summary="Get a list of products",
    responses={200: ProductListSerializer},
)
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductListSerializer


@extend_schema(
    tags=["Product"],
    request=ProductSerializer,
    summary="Create a product",
    responses={200: ProductSerializer},
)
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        tags=['Product'],
        summary="Retrieve product details",
        responses={200: ProductSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        request=ProductSerializer,
        summary="Update product details",
        responses={200: ProductSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        request=ProductSerializer,
        summary="Partially update product details",
        responses={200: ProductSerializer},
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        summary="Delete product",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
