import graphene

import accountInfos.schema
import islands.schema
import buys.schema
import islandReservations.schema

class Query(accountInfos.schema.Query, islands.schema.Query, buys.schema.Query, graphene.ObjectType):
	pass

class Mutation(accountInfos.schema.Mutation, islands.schema.Mutation, buys.schema.Mutation, islandReservations.schema.Mutation, graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)