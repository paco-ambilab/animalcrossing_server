import graphene
import datetime

from graphene_django import DjangoObjectType

from .models import Island

from accountInfos.models import AccountInfo

from accountInfos.schema import AccountInfoType

from django.db.models import Q

class IslandType(DjangoObjectType):
    class Meta:
        model = Island

class CreateIsland(graphene.Mutation):
    id = graphene.Int()
    accountInfo = graphene.Field(AccountInfoType)
    islandPassCode = graphene.String()
    location = graphene.String()
    hashTagDescription = graphene.String()
    reportCount = graphene.Int()
    createTime = graphene.DateTime()
    close = graphene.Boolean()

    class Arguments:
        islandPassCode = graphene.String()
        location = graphene.String()
        hashTagDescription = graphene.String()

    def mutate(self, info, islandPassCode, location, hashTagDescription):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        accountInfo = AccountInfo.objects.filter(user__id__contains=user.id).first()

        if accountInfo is None:
            raise Exception('CreateIsland Fail -> cannot find accountInfo')

        island = Island(
            accountInfo = accountInfo,
            islandPassCode = islandPassCode,
            location = location,
            hashTagDescription = hashTagDescription,
            createTime = datetime.datetime.now().date(),
        )
        island.save()

        return CreateIsland(
            id = island.id,
            accountInfo = island.accountInfo,
            islandPassCode = island.islandPassCode,
            location = island.location,
            hashTagDescription = island.hashTagDescription,
            reportCount = island.reportCount,
            createTime = island.createTime,
            close = island.close,
            )


class ChangeIsland(graphene.Mutation):
    id = graphene.Int()
    accountInfo = graphene.Field(AccountInfoType)
    islandPassCode = graphene.String()
    location = graphene.String()
    hashTagDescription = graphene.String()
    reportCount = graphene.Int()
    createTime = graphene.Date()
    close = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        islandPassCode = graphene.String()
        location = graphene.String()
        hashTagDescription = graphene.String()
        close = graphene.Boolean()

    def mutate(self, info, id, islandPassCode, location, hashTagDescription, close):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        island = Island.objects.get(id = id)

        accountInfo = island.accountInfo
        if accountInfo is None:
            raise Exception('CreateIsland Fail -> cannot find accountInfo')

        if user.id != accountInfo.user.id:
            raise Exception('You are not the correct user!')

        island.islandPassCode = islandPassCode
        island.location = location
        island.hashTagDescription = hashTagDescription
        island.close = close

        island.save()

        return ChangeIsland(
            id = island.id,
            accountInfo = island.accountInfo,
            islandPassCode = island.islandPassCode,
            location = island.location,
            hashTagDescription = island.hashTagDescription,
            reportCount = island.reportCount,
            createTime = island.createTime,
            close = island.close,
            )

class DeleteIsland(graphene.Mutation):
    id = graphene.Int()
    accountInfo = graphene.Field(AccountInfoType)
    islandPassCode = graphene.String()
    location = graphene.String()
    hashTagDescription = graphene.String()
    reportCount = graphene.Int()
    createTime = graphene.Date()
    close = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        island = Island.objects.get(id = id)
        island.delete()

        return DeleteIsland(
            id = island.id,
            accountInfo = island.accountInfo,
            islandPassCode = island.islandPassCode,
            location = island.location,
            hashTagDescription = island.hashTagDescription,
            reportCount = island.reportCount,
            createTime = island.createTime,
            close = island.close,
            )


class Mutation(graphene.ObjectType):
    create_island = CreateIsland.Field()
    change_island = ChangeIsland.Field()
    delete_island = DeleteIsland.Field()

class Query(graphene.ObjectType):
    islands = graphene.List(IslandType, search=graphene.String(), close=graphene.Boolean())

    def resolve_islands(self, info, search=None, close=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if close is None:
            close = False

        if not(search is None):
            filter = (
                Q(location__icontains=search) |
                Q(hashTagDescription__icontains=search) |
                Q(close__icontains=close)
            )
            return Island.objects.filter(filter)

        if search is None:
            filter = (
                Q(close__icontains=close)
            )
            return Island.objects.filter(filter)

        return Island.objects.all()



