from django.contrib import admin

# Register your models here.
from .models import Buy, Product


admin.site.register(Buy)
admin.site.register(Product)
