import graphene
import events.schema


# Query for getting the data from the server.
class Query(events.schema.Query, graphene.ObjectType):
    pass

# Mutation for sending the data to the server.
class Mutation(events.schema.Mutation, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)