from distutils.command.upload import upload
from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=300)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_description2 = models.TextField()
    product_image = models.ImageField(upload_to='media')
    product_front_image = models.ImageField(upload_to='media')
    product_side_image = models.ImageField(upload_to='media')
    product_back_image = models.ImageField(upload_to='media')


class OtherProducts(models.Model):
    product_name = models.CharField(max_length=300)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_description2 = models.TextField()
    product_image = models.ImageField(upload_to='media')
    product_front_image = models.ImageField(upload_to='media')
    product_side_image = models.ImageField(upload_to='media')
    product_back_image = models.ImageField(upload_to='media')
