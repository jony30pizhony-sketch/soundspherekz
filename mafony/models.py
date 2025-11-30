from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Company name")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Country name")
    code = models.CharField(max_length=2, verbose_name="Country code")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class AndroidHeadUnit(models.Model):
    SCREEN_SIZES = [
        ('6.2', '6.2"'),
        ('7', '7"'),
        ('8', '8"'),
        ('9', '9"'),
        ('10.1', '10.1"'),
        ('10.4', '10.4"'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Head unit name")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Manufacturer")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country")
    screen_size = models.CharField(max_length=10, choices=SCREEN_SIZES, verbose_name="Screen size")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    android_version = models.CharField(max_length=50, verbose_name="Android version")
    ram = models.CharField(max_length=20, verbose_name="RAM")
    storage = models.CharField(max_length=20, verbose_name="Storage")
    image = models.ImageField(upload_to='headunits/', verbose_name="Image", blank=True, null=True)
    in_stock = models.BooleanField(default=True, verbose_name="In stock")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"
    
    class Meta:
        verbose_name = "Android Head Unit"
        verbose_name_plural = "Android Head Units"

# ”прощенные модели дл€ демонстрации
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(AndroidHeadUnit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(AndroidHeadUnit)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist for {self.user.username}"