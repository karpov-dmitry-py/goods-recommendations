from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Product, Property, ProductProperty, CategoryKeyProperty
from .serializers import CategorySerializer, ProductSerializer, PropertySerializer, ProductPropertySerializer, \
    CategoryKeyPropertySerializer


def check_product_props(current_product, key_props):
    prod_props = current_product.properties.filter(property__in=key_props)
    return {
        'prod_props': prod_props,
        'mismatch': len(prod_props) < len(key_props),  # check if product misses some of its category key props
    }


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
            row['row_id'] = property_row.id
            row['property_id'] = property_row.property.id
            row['property_name'] = property_row.property.name
            result.append(row)
        data = {'key_properties': result}
        return Response(data=data)

    @action(detail=False)
    def recommendations(self, request):

        max_price_delta = request.query_params.get('price_delta')
        try:
            max_price_delta = float(max_price_delta)
        except (TypeError, ValueError):
            max_price_delta = 30.00

        result = []
        for category in Category.objects.all():

            cat_key_props = category.key_properties.all()
            cat_props = [cat_key_prop.property for cat_key_prop in cat_key_props]
            cat_prods_props = {}

            for product in category.products.all():

                key_props = []
                similar_products = []
                cat_prods_props[product.id] = {
                    'product_id': product.id,
                    'product_name': product.name,
                    'product_price': product.price,
                    'key_props': key_props,
                    'similar_products': similar_products,
                }

                prod_data = check_product_props(product, cat_props)
                prod_props = prod_data['prod_props']
                mismatch = prod_data['mismatch']
                if mismatch:
                    continue

                # product key props values
                for property_row in prod_props.all():
                    row = {}
                    row['property_id'] = property_row.property.id
                    row['property_name'] = property_row.property.name
                    row['property_value'] = property_row.value
                    key_props.append(row)
                cat_prods_props[product.id]['key_props'] = key_props

                # similar products
                prod_props_values = {}
                for prod_prop_row in prod_props:
                    prod_props_values[prod_prop_row.property.id] = prod_prop_row.value

                for curr_product in category.products.exclude(id=product.id):
                    price_delta = (product.price - curr_product.price) / product.price * 100
                    price_delta = -price_delta if price_delta < 0 else price_delta
                    price_delta = round(price_delta, 2)

                    # price delta exceeds max allowed value
                    if price_delta > max_price_delta:
                        continue

                    curr_prod_data = check_product_props(curr_product, cat_props)
                    curr_prod_props = curr_prod_data['prod_props']
                    curr_mismatch = curr_prod_data['mismatch']
                    if curr_mismatch:
                        continue

                    for curr_property_row in curr_prod_props:
                        # curr prod prop value did not match pivot prod prop value
                        if curr_property_row.value != prod_props_values[curr_property_row.property.id]:
                            break
                    else:
                        similar_products.append({
                            'product_id': curr_product.id,
                            'product_name': curr_product.name,
                            'product_price': curr_product.price,
                            'product_price_delta': price_delta,
                        })

                cat_prods_props[product.id]['similar_products'] = similar_products

            result.append({
                'category_id': category.id,
                'category_name': category.name,
                'products': cat_prods_props,
            })

        return Response(data=result)


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
            row['row_id'] = property_row.id
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
