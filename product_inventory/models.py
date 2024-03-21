from django.db import models


class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_of_workday = models.TimeField()
    end_of_workday = models.TimeField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='product_category')
    enterprise = models.ForeignKey(Enterprise,
                                   on_delete=models.CASCADE,
                                   related_name='product_enterprise')

    def __str__(self):
        return self.name
