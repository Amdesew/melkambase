from django.db import models

class samples(models.Model):
    item_img = models.ImageField()
    item_title = models.CharField(max_length=50)
    item_disc = models.CharField(max_length=50)

class natural_products(samples):
    pass

class car_spare_part(models.Model):
    item_img = models.ImageField()
    item_title = models.CharField(max_length=50)
    item_disc = models.CharField(max_length=50)

class orders(models.Model):
    user_name = models.CharField(max_length=50)
    orderd_item = models.CharField(max_length=50)
    amount_item = models.CharField(max_length=50)
    user_number = models.CharField(max_length=50)