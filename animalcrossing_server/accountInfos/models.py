from django.db import models
from django.conf import settings

class AccountInfo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='acountInfos', on_delete=models.CASCADE)
    createTime = models.DateField()
    islandOwnerID = models.CharField(max_length=100)
