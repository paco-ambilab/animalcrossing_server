import graphene

from graphene_django import DjangoObjectType

from .models import Buy

class BuyType(DjangoObjectType):
    class Meta:
        model = Buy
