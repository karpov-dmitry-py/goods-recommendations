from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Product, Property, ProductProperty, CategoryKeyProperty
from .serializers import CategorySerializer, ProductSerializer, PropertySerializer, ProductPropertySerializer, \
    CategoryKeyPropertySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=True)
    def products(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        products = category.products.all()
        result = []
        for product in products:
            row = {}
            row['product_id'] = product.id
            row['product_name'] = product.name
            row['product_description'] = product.description
            row['product_price'] = product.price
            result.append(row)
        data = {'products': result}
        return Response(data=data)

    @action(detail=True)
    def key_properties(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        properties = category.key_properties.all()
        result = []
        for property_row in properties:
            row = {}
            row['property_id'] = property_row.property.id
            row['property_name'] = property_row.property.name
            result.append(row)
        data = {'key_properties': result}
        return Response(data=data)

    @action(detail=False)
    def recommendations(self, request):
        result = []
        for category in Category.objects.all():
            row = {}
            row['id'] = category.id
            row['name'] = category.name
            result.append(row)
        data = {'recommendations': result}
        return Response(data=data)


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=True)
    def properties(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        properties = product.properties.all()
        result = []
        for property_row in properties:
            row = {}
            row['property_id'] = property_row.property.id
            row['property_name'] = property_row.property.name
            row['property_value'] = property_row.value
            result.append(row)
        data = {'properties': result}
        return Response(data=data)


class PropertyViewSet(ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    @action(detail=True)
    def products(self, request, pk=None):
        property = get_object_or_404(Property, pk=pk)
        products = property.products.all()
        result = []
        for property_row in products:
            row = {}
            row['product_id'] = property_row.product.id
            row['product_name'] = property_row.product.name
            row['property_id'] = property_row.property.id
            row['property_name'] = property_row.property.name
            row['property_value'] = property_row.value
            result.append(row)
        data = {'properties': result}
        return Response(data=data)


class ProductPropertyViewSet(ModelViewSet):
    serializer_class = ProductPropertySerializer
    queryset = ProductProperty.objects.all()


class CategoryKeyPropertyViewSet(ModelViewSet):
    serializer_class = CategoryKeyPropertySerializer
    queryset = CategoryKeyProperty.objects.all()
