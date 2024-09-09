from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    
def __str__(self):
    return self.name