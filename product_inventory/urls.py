from django.urls import path
from .views import (EnterpriseListAPIView, EnterpriseCreateAPIView, EnterpriseUpdateDeleteAPIView, CategoryListAPIView,
                    CategoryCreateAPIView, CategoryUpdateDeleteAPIView, ProductListAPIView, ProductCreateAPIView,
                    ProductUpdateDeleteAPIView)

urlpatterns = [
    path('enterprises/', EnterpriseListAPIView.as_view(), name='enterprise_list'),
    path('add_enterprise/', EnterpriseCreateAPIView.as_view(), name='create_enterprise'),
    path('enterprise/<int:pk>/', EnterpriseUpdateDeleteAPIView.as_view(), name='enterprise'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('add_category/', CategoryCreateAPIView.as_view(), name='create_category'),
    path('category/<int:pk>/', CategoryUpdateDeleteAPIView.as_view(), name='category'),
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('add_product/', ProductCreateAPIView.as_view(), name='create_product'),
    path('product/<int:pk>/', ProductUpdateDeleteAPIView.as_view(), name='product'),
]
