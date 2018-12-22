from estadisticas.models import Estadistica
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

class EstadisticaNode(DjangoObjectType):
    class Meta:
        model = Estadistica
        interfaces = (Node, )

class Query(ObjectType):
    estadistica = Node.Field(EstadisticaNode)
    all_estadisticas = DjangoConnectionField(EstadisticaNode)