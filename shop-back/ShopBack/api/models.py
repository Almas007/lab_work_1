from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def name_starts_with_a(self):
        return self.name.startswith('a')


class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products')
    prod_name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.prod_name
