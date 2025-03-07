from django.contrib.auth.models import AbstractUser
from django.db import models

#custom user types farmer and buyer
class CustomUser(AbstractUser):
    USER_TYPES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='buyer')

    def __str__(self):
        return self.username
    
#for crop listing
class Crop(models.Model):
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    expected_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.farmer.username}"
