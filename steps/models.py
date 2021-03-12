from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Steps(models.Model):
    steps = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(50000)])
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.owner) + " " + str(self.date) + " " + str(self.steps))