import graphene

import productionapp.schema


class Query(productionapp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)