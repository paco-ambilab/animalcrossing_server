from django.db import models
from django.conf import settings

class AccountInfo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    islandOwnerID = models.CharField(max_length=100)
