from django.contrib import admin

from .models import Product
from .models import Invoice

admin.site.register(Product)
admin.site.register(Invoice)