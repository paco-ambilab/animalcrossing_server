import graphene
import datetime

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

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
    
    return CreateAccount(accountInfo=accountInfo)
