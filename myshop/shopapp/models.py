from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
