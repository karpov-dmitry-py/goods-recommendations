from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'Categories'

    name = models.CharField(max_length=200)

    def __str__(self):
        return f'ID: {self.id}. {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f'ID: {self.id}. {self.name}. price: {self.price}'


class Property(models.Model):
    class Meta:
        db_table = 'Properties'

    name = models.CharField(max_length=150)

    def __str__(self):
        return f'ID: {self.id}. {self.name}'


class ProductProperty(models.Model):
    class Meta:
        db_table = 'Product_properties'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='products')
    value = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.product}: {self.property} -> {self.value}'


class CategoryKeyProperty(models.Model):
    class Meta:
        db_table = 'Category_key_properties'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='key_properties')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f'{self.category} -> {self.property}'
