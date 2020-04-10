
from django.db import models
from django.conf import settings

class Buy(models.Model):

    accountInfo = models.ForeignKey('accountInfos.AccountInfo', related_name='postedBuys', on_delete=models.CASCADE)
    islandPassCode = models.TextField(blank=True)
    itemName = models.TextField(blank=True)
    numberOfItem = models.IntegerField(default=1)
    unitPrice = models.IntegerField(default=0)
    reportCount = models.IntegerField(default=0)
    createTime = models.TimeField(auto_now=True)
    close = models.BooleanField(default=False)
