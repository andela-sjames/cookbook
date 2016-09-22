import graphene

import ingredients.schema
from graphene.contrib.django.debug import DjangoDebugMiddleware


class Query(ingredients.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(name='Cookbook Schema')
schema.query = Query
schema.middlewares = [DjangoDebugMiddleware()]
