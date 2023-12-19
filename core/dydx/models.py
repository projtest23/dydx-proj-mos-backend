from django.db import models
from django.contrib.auth.models import User


class Positions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    market = models.CharField(max_length=255,default='ETH-USD')
    long = models.BooleanField(default=True)
    size = models.FloatField()
    leverage = models.FloatField()
    realized_PL = models.FloatField()
    average_open = models.FloatField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    


class Balance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    balance= models.FloatField()
    account_leverage = models.FloatField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    uniswap = models.BooleanField(default=True)
    wallet_address = models.CharField(max_length=500,null=True)
