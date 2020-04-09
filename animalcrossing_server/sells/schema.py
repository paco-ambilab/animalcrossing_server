import graphene

from graphene_django import DjangoObjectType

from .models import Sell

class SellType(DjangoObjectType):
    class Meta:
        model = Sell
