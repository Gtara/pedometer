from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Steps(models.Model):
    steps = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(50000)])
    date = models.DateField()