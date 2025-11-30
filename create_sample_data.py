# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soundphereProject.settings')
django.setup()

from mafony.models import Manufacturer, Country, AndroidHeadUnit

def create_sample_data():
    print("Starting to create sample data...")
    
    # Create manufacturers
    manufacturers_data = [
        {"name": "Pioneer"},
        {"name": "Sony"},
        {"name": "Kenwood"},
        {"name": "Alpine"},
        {"name": "JVC"},
    ]
    
    manufacturers = []
    for data in manufacturers_data:
        manufacturer, created = Manufacturer.objects.get_or_create(**data)
        manufacturers.append(manufacturer)
        print(f"Created manufacturer: {manufacturer.name}")
    
    # Create countries
    countries_data = [
        {"name": "Japan", "code": "JP"},
        {"name": "China", "code": "CN"},
        {"name": "Germany", "code": "DE"},
        {"name": "South Korea", "code": "KR"},
    ]
    
    countries = []
    for data in countries_data:
        country, created = Country.objects.get_or_create(**data)
        countries.append(country)
        print(f"Created country: {country.name}")
    
    # Create head units
    headunits_data = [
        {
            "name": "X7000 Android",
            "manufacturer": manufacturers[0],
            "country": countries[0],
            "screen_size": "7",
            "price": 25990,
            "description": "Advanced Android head unit with 7-inch display, 4GB RAM, and 64GB storage. Perfect for modern cars with support for Android Auto and Apple CarPlay.",
            "android_version": "11",
            "ram": "4GB",
            "storage": "64GB",
            "in_stock": True
        },
        {
            "name": "Z9000 Pro",
            "manufacturer": manufacturers[1],
            "country": countries[0],
            "screen_size": "10.1",
            "price": 42990,
            "description": "Premium Android head unit with large 10.1-inch display, 8GB RAM, and 128GB storage. Features high-quality audio and advanced connectivity options.",
            "android_version": "12",
            "ram": "8GB",
            "storage": "128GB",
            "in_stock": True
        },
        {
            "name": "A5000 Basic",
            "manufacturer": manufacturers[2],
            "country": countries[1],
            "screen_size": "6.2",
            "price": 18490,
            "description": "Budget-friendly Android head unit with 6.2-inch display. Great value for money with all essential features.",
            "android_version": "10",
            "ram": "2GB",
            "storage": "32GB",
            "in_stock": True
        },
        {
            "name": "B8000 Ultra",
            "manufacturer": manufacturers[3],
            "country": countries[2],
            "screen_size": "8",
            "price": 35790,
            "description": "High-performance Android head unit from Germany with 8-inch display and premium build quality.",
            "android_version": "11",
            "ram": "6GB",
            "storage": "128GB",
            "in_stock": False
        },
        {
            "name": "C3000 Smart",
            "manufacturer": manufacturers[4],
            "country": countries[3],
            "screen_size": "9",
            "price": 28990,
            "description": "Smart Android head unit with 9-inch display and excellent audio quality from JVC.",
            "android_version": "11",
            "ram": "4GB",
            "storage": "64GB",
            "in_stock": True
        },
    ]
    
    for data in headunits_data:
        headunit, created = AndroidHeadUnit.objects.get_or_create(
            name=data["name"],
            defaults=data
        )
        if created:
            print(f"Created head unit: {headunit.name}")
        else:
            print(f"Head unit already exists: {headunit.name}")
    
    print("Sample data creation completed!")
    print(f"Total manufacturers: {Manufacturer.objects.count()}")
    print(f"Total countries: {Country.objects.count()}")
    print(f"Total head units: {AndroidHeadUnit.objects.count()}")

if __name__ == "__main__":
    create_sample_data()