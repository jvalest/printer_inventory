from django.contrib import admin
from .models import inventory_entry, toner
# Register your models here.

admin.site.register(inventory_entry)
admin.site.register(toner)