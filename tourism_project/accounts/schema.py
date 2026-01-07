import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)   # اضافه شد
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, username, email, password):
        user = User(username=username, email=email)  # مقدار ایمیل داده شده
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
