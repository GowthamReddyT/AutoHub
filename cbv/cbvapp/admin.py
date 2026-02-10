from django.contrib import admin
from .models import Company, Exterior, Interior,Product

# Register your models here.
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Interior)
admin.site.register(Exterior)

