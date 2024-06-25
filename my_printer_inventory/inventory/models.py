from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class inventory_entry(models.Model):
    item_name = models.CharField(max_length=255)
    item_link = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.item_name
    
class toner(models.Model):
    item_name = models.CharField(max_length=255)
    model_used_for = models.CharField(max_length=255)
    item_link = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.item_name    