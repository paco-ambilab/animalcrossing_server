import graphene

from graphene_django import DjangoObjectType

from .models import AccountInfo

class AccountInfoType(DjangoObjectType):
    class Meta:
        model = AccountInfo

