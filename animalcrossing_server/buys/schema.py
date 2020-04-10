import graphene
import datetime

from graphene_django import DjangoObjectType

from .models import Buy

from accountInfos.models import AccountInfo 

from accountInfos.schema import AccountInfoType

from django.db.models import Q

class BuyType(DjangoObjectType):
    class Meta:
        model = Buy


class CreateBuy(graphene.Mutation):
    id = graphene.Int()
    accountInfo = graphene.Field(AccountInfoType)
    islandPassCode = graphene.String()
    itemName = graphene.String()
    numberOfItem = graphene.Int()
    unitPrice = graphene.Int()
    reportCount = graphene.Int()
    createTime = graphene.DateTime()
    close = graphene.Boolean()

    class Arguments:
        islandPassCode = graphene.String()
        itemName = graphene.String()
        numberOfItem = graphene.Int()
        unitPrice = graphene.Int()

    def mutate(self, info, islandPassCode, itemName, numberOfItem, unitPrice):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        accountInfo = AccountInfo.objects.filter(user__id__contains=user.id).first()

        if accountInfo is None:
            raise Exception('CreateIsland Fail -> cannot find accountInfo')

        buy = Buy(
            accountInfo = accountInfo,
            islandPassCode = islandPassCode,
            itemName = itemName,
            numberOfItem = numberOfItem,
            unitPrice = unitPrice,
            createTime = datetime.datetime.now(),
        )
        buy.save()

        return CreateBuy(
            id = buy.id,
            accountInfo = buy.accountInfo,
            islandPassCode = buy.islandPassCode,
            itemName = buy.itemName,
            numberOfItem = buy.numberOfItem,
            unitPrice = buy.unitPrice,
            reportCount = buy.reportCount,
            createTime = buy.createTime,
            close = buy.close,
            )

class ChangeBuy(graphene.Mutation):
    id = graphene.Int()
    accountInfo = graphene.Field(AccountInfoType)
    islandPassCode = graphene.String()
    itemName = graphene.String()
    numberOfItem = graphene.Int()
    unitPrice = graphene.Int()
    reportCount = graphene.Int()
    createTime = graphene.DateTime()
    close = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        islandPassCode = graphene.String()
        itemName = graphene.String()
        numberOfItem = graphene.Int()
        unitPrice = graphene.Int()
        close = graphene.Boolean()

    def mutate(self, info, id, islandPassCode, itemName, numberOfItem, unitPrice, close):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        buy = Buy.objects.get(id = id)

        accountInfo = buy.accountInfo
        if accountInfo is None:
            raise Exception('CreateIsland Fail -> cannot find accountInfo')

        if user.id != accountInfo.user.id:
            raise Exception('You are not the correct user!')

        buy.islandPassCode = islandPassCode
        buy.itemName = itemName
        buy.numberOfItem = numberOfItem
        buy.unitPrice = unitPrice
        buy.close = close

        buy.save()

        return ChangeBuy(
            id = buy.id,
            accountInfo = buy.accountInfo,
            islandPassCode = buy.islandPassCode,
            itemName = buy.itemName,
            numberOfItem = buy.numberOfItem,
            unitPrice = buy.unitPrice,
            reportCount = buy.reportCount,
            createTime = buy.createTime,
            close = buy.close,
            )


class DeleteBuy(graphene.Mutation):
    id = graphene.Int()
    accountInfo = graphene.Field(AccountInfoType)
    islandPassCode = graphene.String()
    itemName = graphene.String()
    numberOfItem = graphene.Int()
    unitPrice = graphene.Int()
    reportCount = graphene.Int()
    createTime = graphene.DateTime()
    close = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        buy = Buy.objects.get(id = id)
        buy.delete()
        
        return DeleteBuy(
            id = buy.id,
            accountInfo = buy.accountInfo,
            islandPassCode = buy.islandPassCode,
            itemName = buy.itemName,
            numberOfItem = buy.numberOfItem,
            unitPrice = buy.unitPrice,
            reportCount = buy.reportCount,
            createTime = buy.createTime,
            close = buy.close,
            )


class Mutation(graphene.ObjectType):
    create_buy = CreateBuy.Field()
    change_buy = ChangeBuy.Field()
    delete_buy = DeleteBuy.Field()

class Query(graphene.ObjectType):
    buys = graphene.List(BuyType, search=graphene.String(), close=graphene.Boolean())

    def resolve_buys(self, info, search=None, close=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if close is None:
            close = False

        if not(search is None):
            filter = (
                Q(itemName__icontains=search) |
                Q(close__icontains=close)
            )
            return Buy.objects.filter(filter)

        if search is None:
            filter = (
                Q(close__contains=close)
            )
            return Buy.objects.filter(filter)

        return Buy.objects.all()

