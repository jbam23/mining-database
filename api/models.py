from django.db import models

# Create your models here.
class Miner(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    facility = models.CharField(max_length=32, default="", unique=False)
    machineName = models.CharField(max_length=32, default="", unique=False)
    quantity = models.IntegerField(null=False, default=1)
    power = models.IntegerField(null=False, default=1)
    monthlyFee = models.IntegerField(null=False,default=1)
    miningPool = models.CharField(max_length=32, default="", unique=False)
    status = models.CharField(max_length=32,default="", unique=False)
