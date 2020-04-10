import datetime

from django.db import models
from django.conf import settings

class Island(models.Model):

    accountInfo = models.ForeignKey('accountInfos.AccountInfo', related_name='postedIslands', on_delete=models.CASCADE)
    islandPassCode = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, null=True)
    hashTagDescription = models.TextField(blank=True, null=True)
    reportCount = models.IntegerField(default=0, null=True)
    createTime = models.DateTimeField(auto_now=True, null=True)
    close = models.BooleanField(default=False, null=True)

