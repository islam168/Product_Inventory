from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers


class EnterpriseService:
    @staticmethod
    def format_work_hours(start_time, end_time) -> str:
        return f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"


class ProductService:
    @staticmethod
    def validate_product_data(data):
        if data['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative")
        if data['stock_quantity'] < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative")


# Pagination
class LargePagination(PageNumberPagination):
    page_size = 10  # Количество записей на одной странице

