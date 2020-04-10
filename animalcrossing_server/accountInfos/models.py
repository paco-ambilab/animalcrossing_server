
from django.db import models
from django.conf import settings

class AccountInfo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='acountInfos', on_delete=models.CASCADE)
    switchID = models.TextField(blank=True)
    createTime = models.TimeField(auto_now=True)
