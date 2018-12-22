import graphene
import estadisticas.schema
import reportes.schema
import tareas.schema

class Query(estadisticas.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)