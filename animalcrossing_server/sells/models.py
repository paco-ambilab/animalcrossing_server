from django.db import models
from django.conf import settings
    
class Sell(models.Model):

    accountInfo = models.ForeignKey('accountInfos.AccountInfo', related_name='postedSells', on_delete=models.CASCADE)
    hashTagDescription = models.TextField(blank=True)
    reportCount = models.IntegerField(default=0)
    createTime = models.DateField()
    close = models.BooleanField(default=False)
