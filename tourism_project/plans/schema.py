import graphene
from graphene_django import DjangoObjectType
from .models import Plan
from accounts.models import User
from destinations.models import Destination

class PlanType(DjangoObjectType):
    class Meta:
        model = Plan
        fields = ("id", "title", "description", "user", "destinations")

class Query(graphene.ObjectType):
    all_plans = graphene.List(PlanType)
    plans_by_user = graphene.List(PlanType, user_id=graphene.Int())

    def resolve_all_plans(root, info):
        return Plan.objects.all()

    def resolve_plans_by_user(root, info, user_id):
        return Plan.objects.filter(user__id=user_id)

class CreatePlan(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String(default_value="یک برنامه سفر آزمایشی")
        destination_ids = graphene.List(graphene.Int)

    plan = graphene.Field(PlanType)

    def mutate(root, info, user_id, title, description, destination_ids=[]):
        user = User.objects.get(id=user_id)
        plan = Plan(user=user, title=title, description=description)
        plan.save()
        if destination_ids:
            destinations = Destination.objects.filter(id__in=destination_ids)
            plan.destinations.set(destinations)
        return CreatePlan(plan=plan)

class Mutation(graphene.ObjectType):
    create_plan = CreatePlan.Field()
