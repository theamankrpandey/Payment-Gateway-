from django.db import models

# Create your models here.
class Order(models.Model):
    Order_id = models.CharField(max_length=200)
    Amount = models.IntegerField()
    Razorpay_Id = models.CharField(max_length=200)
    Status = models.BooleanField(default=False)