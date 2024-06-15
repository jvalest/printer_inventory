from django.db import models

# Create your models here.
class inventory_entry(models.Model):
    item_name = models.CharField(max_length=255)
    item_link = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
