import datetime

from django.db import models
from django.conf import settings

class IslandReservation(models.Model):
    island = models.ForeignKey('islands.Island', related_name='reservation', on_delete=models.CASCADE)
    accountInfo = models.ForeignKey('accountInfos.AccountInfo', related_name='reservedIslands', on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now=True, null=True)
