from django.db import models
from user.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    is_paid = models.BooleanField(default=False)