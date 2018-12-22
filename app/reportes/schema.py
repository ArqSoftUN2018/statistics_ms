from reportes.models import Reporte
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

class ReporteNode(DjangoObjectType):
    class Meta:
        model = Reporte
        interfaces = (Node, )

class Query(ObjectType):
    reporte = Node.Field(ReporteNode)
    all_reportes = DjangoConnectionField(ReporteNode)