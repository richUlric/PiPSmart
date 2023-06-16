from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class ReservationParking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()  # Remove the input_formats argument
    time = models.TimeField()  # Remove the input_formats argument
    # Add other fields as needed

# Create your models here.
