from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid  
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name