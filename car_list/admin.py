from django.contrib import admin

# Register your models here.
from .models import Car

class CarAdmin(admin.ModelAdmin):
    search_fields = ['make', 'model', 'year', 'color']
    list_display = ['make', 'year']
    list_filter = ['make', 'year', 'color']

admin.site.register(Car, CarAdmin)
