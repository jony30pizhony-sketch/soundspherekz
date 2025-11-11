from django.contrib import admin
from .models import AndroidHeadUnit, Manufacturer, Country

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(AndroidHeadUnit)
class AndroidHeadUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'country', 'screen_size', 'price', 'in_stock']
    list_filter = ['manufacturer', 'country', 'screen_size', 'in_stock']
    search_fields = ['name', 'manufacturer__name']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'manufacturer', 'country', 'description')
        }),
        ('Specifications', {
            'fields': ('screen_size', 'android_version', 'ram', 'storage')
        }),
        ('Commercial Information', {
            'fields': ('price', 'in_stock', 'image')
        }),
        ('Additional', {
            'fields': ('created_at',)
        }),
    )