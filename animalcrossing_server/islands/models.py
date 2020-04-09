from django.db import models
from django.conf import settings

class Island(models.Model):

    accountInfo = models.ForeignKey('accountInfos.AccountInfo', related_name='postedIslands', on_delete=models.CASCADE)
    islandPassCode = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    hashTagDescription = models.TextField(blank=True)
    reportCount = models.IntegerField(default=0)
    createTime = models.DateField()
    close = models.BooleanField(default=False)

