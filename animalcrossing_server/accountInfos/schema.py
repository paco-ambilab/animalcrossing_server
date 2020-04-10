import graphene
import datetime
import graphql_jwt

from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from .models import AccountInfo

class AccountInfoType(DjangoObjectType):
    class Meta:
        model = AccountInfo
        
class CreateAccount(graphene.Mutation):
    accountInfo = graphene.Field(AccountInfoType)
    
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email, switchID):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        accountInfo = AccountInfo(
            user = user,
            createTime = datetime.datetime.now().date(),
            switchID = switchID
        )
        accountInfo.save()

        return CreateAccount(accountInfo=accountInfo)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_account = CreateAccount.Field()


class Query(graphene.ObjectType):
    account = graphene.Field(AccountInfoType)

    def resolve_account(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged first!')

        accountInfo = AccountInfo.objects.filter(user__id__contains=user.id).first()

        if accountInfo is None:
            raise Exception('Get accountInfo fail -> null accountInfo!')

        return accountInfo



