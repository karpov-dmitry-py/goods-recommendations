from rest_framework.serializers import ModelSerializer
from .models import Category, Product, Property, ProductProperty, CategoryKeyProperty


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class ProductPropertySerializer(ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = '__all__'


class CategoryKeyPropertySerializer(ModelSerializer):
    class Meta:
        model = CategoryKeyProperty
        fields = '__all__'
