import graphene
from graphene_django import DjangoObjectType
from .models import Destination
from decimal import Decimal

class DestinationType(DjangoObjectType):
    class Meta:
        model = Destination
        fields = ("id", "name", "description", "city", "price")

class Query(graphene.ObjectType):
    all_destinations = graphene.List(DestinationType)
    destinations_by_city = graphene.List(DestinationType, city=graphene.String())

    def resolve_all_destinations(root, info):
        return Destination.objects.all()

    def resolve_destinations_by_city(root, info, city):
        return Destination.objects.filter(city__icontains=city)

class CreateDestination(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        city = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Float()  # همچنان Float می‌گیریم از GraphQL

    destination = graphene.Field(DestinationType)

    def mutate(root, info, name, city, description=None, price=None):
        from decimal import Decimal
        if price is not None:
            price = Decimal(str(price))  # تبدیل به Decimal
        destination = Destination(
            name=name,
            city=city,
            description=description,
            price=price
        )
        destination.save()
        return CreateDestination(destination=destination)


class Mutation(graphene.ObjectType):
    create_destination = CreateDestination.Field()
