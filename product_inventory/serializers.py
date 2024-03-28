from rest_framework import serializers
from .models import Enterprise, Category, Product
from .services import EnterpriseService, ProductService


# Serializer for Get requests
class EnterpriseListSerializer(serializers.ModelSerializer):
    work_hours = serializers.SerializerMethodField()

    class Meta:
        model = Enterprise
        fields = ['id', 'name', 'description', 'work_hours', 'address']

    def get_work_hours(self, obj) -> str:
        return EnterpriseService.format_work_hours(obj.start_of_workday, obj.end_of_workday)


class EnterpriseSerializer(serializers.ModelSerializer):
    start_of_workday = serializers.TimeField(format="%H:%M")
    end_of_workday = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Enterprise
        fields = ['id', 'name', 'description', 'start_of_workday', 'end_of_workday', 'address']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductListSerializer(serializers.ModelSerializer):
    enterprise = serializers.CharField(source='enterprise.name', read_only=True)  # Извлечения название предприятия
    # на котором произведен продукт из enterprise
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'category', 'enterprise']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'category', 'enterprise']

    def validate(self, data):
        ProductService.validate_product_data(data)
        return data
