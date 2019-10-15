from django.db import models

class Category(models.Model):
    # CategoryID = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    CategoryName = models.CharField(max_length=50, unique=True)

class Product(models.Model):
    ProductCode = models.CharField(max_length=50)
    ProductName = models.CharField(max_length=50)
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ProductQuantity = models.IntegerField()

class CategoryProduct(models.Model):
    CategoryID = models.ForeignKey('Category', on_delete=models.CASCADE)
    ProductID = models.ForeignKey('Product', on_delete=models.CASCADE)
