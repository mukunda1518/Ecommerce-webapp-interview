from django.db import models

# Create your models here.


Quality_CHOICES = [
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low")
]


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.IntegerField()
    image = models.ImageField()
    rating = models.IntegerField(null=True, blank=True)
    quality = models.CharField(max_length=10, choices=Quality_CHOICES, default="Medium")


class Color(models.Model):
    name = models.CharField(max_length=20)
    hex_code = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)

