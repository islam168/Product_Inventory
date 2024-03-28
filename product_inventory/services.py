from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from rest_framework.response import Response


class EnterpriseService:
    @staticmethod
    def format_work_hours(start_time, end_time) -> str:
        """
        Static method to format work hours into a string.

        Args:
            start_time: Start time of workday.
            end_time: End time of workday.

        Returns:
            str: Formatted work hours string.
        """
        return f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"


class ProductService:
    @staticmethod
    def validate_product_data(data):
        """
        Static method to validate product data.

        Args:
            data (dict): Dictionary containing product data.

        Raises:
            serializers.ValidationError: If price or stock_quantity is negative.
        """
        if data['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative")
        if data['stock_quantity'] < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative")


# Pagination
class NoMetadataPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)

