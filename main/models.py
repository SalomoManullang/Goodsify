from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid  
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID for product ID
    name = models.CharField(max_length=255)  # Product name
    price = models.IntegerField()  # Price of the product
    description = models.TextField()  # Product description
    rating = models.PositiveSmallIntegerField(  # Rating field with validators
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user who owns the product
    stok = models.IntegerField()  # Stock available for the product
    image_url = models.URLField(max_length=500, null=True, blank=True)  # Optional image URL for the product
    city = models.CharField(max_length=100)  # City where the product is located

    def __str__(self):
        return self.name
