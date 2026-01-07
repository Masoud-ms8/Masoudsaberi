import graphene
import accounts.schema
import destinations.schema
import plans.schema

class Query(accounts.schema.Query,
            destinations.schema.Query,
            plans.schema.Query,
            graphene.ObjectType):
    pass

class Mutation(accounts.schema.Mutation,
               destinations.schema.Mutation,
               plans.schema.Mutation,
               graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
