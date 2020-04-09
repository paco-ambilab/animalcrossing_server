import graphene
import datetime

from graphene_django import DjangoObjectType

from .models import Island

from accountInfos.schema import AccountInfoType

class IslandType(DjangoObjectType):
    class Meta:
        model = Island

class CreateIsland(graphene.Mutation):
    accountInfo = graphene.Field(UserType)
    islandPassCode = graphene.String()
    location = graphene.String()
    hashTagDescription = graphene.String()
    reportCount = graphene.Int()
    createTime = graphene.Date()
    close = graphene.Boolean()

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, islandPassCode, location, hashTagDescription):
        user = info.context.user or None
        if not (user is None):
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        accountInfo = AccountInfo.objects.filter(user__id__contains=user.id).first()

        if not(accountInfo is None):
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
            accountInfo = island.accountInfo,
            islandPassCode = island.islandPassCode,
            location = island.location,
            hashTagDescription = island.hashTagDescription,
            reportCount = island.reportCount,
            createTime = island.createTime,
            close = island.close
            )



class Mutation(graphene.ObjectType):
    create_island = CreateIsland.Field()

