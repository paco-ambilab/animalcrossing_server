import graphene
import datetime

from graphene_django import DjangoObjectType

from .models import IslandReservation

from accountInfos.models import AccountInfo
from islands.models import Island

from accountInfos.schema import AccountInfoType
from islands.schema import IslandType

from django.db.models import Q

class IslandReservationType(DjangoObjectType):
    class Meta:
        model = IslandReservation

class CreateIslandReservation(graphene.Mutation):
    id = graphene.Int()
    island = graphene.Field(IslandType)
    accountInfo = graphene.Field(AccountInfoType)
    createTime = graphene.DateTime()

    class Arguments:
        islandID = graphene.String()

    def mutate(self, info, islandID):
        user = info.context.user or None

        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        accountInfo = AccountInfo.objects.filter(user__id__contains=user.id).first()

        if accountInfo is None:
            raise Exception('CreateIslandReservation Fail -> cannot find accountInfo')

        if islandID is None:
            raise Exception('CreateIslandReservation Fail -> islandID is null')

        island = Island.objects.filter(id__contains=islandID).first()

        if island is None:
            raise Exception('CreateIslandReservation Fail -> cannot find island')

        islandReservation = IslandReservation(
            island = island,
            accountInfo = accountInfo,
            createTime = datetime.datetime.now(),
        )
        island.save()

        return CreateIslandReservation(
            id = islandReservation.id,
            island = islandReservation.island,
            accountInfo = islandReservation.accountInfo,
            createTime = islandReservation.createTime,
            )

class DeleteIslandReservation(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        islandID = graphene.Int()

    def mutate(self, info, islandID):
        user = info.context.user or None
        if user is None:
            raise Exception('You must be logged first!')
        
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        accountInfo = AccountInfo.objects.filter(user__id__contains=user.id).first()

        if accountInfo is None:
            raise Exception('CreateIslandReservation Fail -> cannot find accountInfo')

        island = Island.objects.get(id=islandID)

        if island is None:
            raise Exception('CreateIslandReservation Fail -> cannot find island')


        filter = (
                Q(island=island) &
                Q(accountInfo=accountInfo)
            )

        islandReservation = IslandReservation.objects.filter(filter).first()

        if not(islandReservation is None):
            islandReservation.delete()

        return DeleteIslandReservation(
            id = islandReservation.id,
            )


class Mutation(graphene.ObjectType):
    create_island_reservation = CreateIslandReservation.Field()
    delete_island_reservation = DeleteIslandReservation.Field()



