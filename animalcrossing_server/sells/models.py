
from django.db import models
from django.conf import settings
    
class Sell(models.Model):

    accountInfo = models.ForeignKey('accountInfos.AccountInfo', related_name='postedSells', on_delete=models.CASCADE)
    islandPassCode = models.TextField(blank=True, null=True)
    itemName = models.TextField(blank=True, null=True)
    numberOfItem = models.IntegerField(default=1, null=True)
    unitPrice = models.IntegerField(default=0, null=True)
    reportCount = models.IntegerField(default=0, null=True)
    createTime = models.DateTimeField(auto_now=True, null=True)
    close = models.BooleanField(default=False, null=True)
