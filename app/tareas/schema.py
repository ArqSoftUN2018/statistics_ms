from tareas.models import Tarea
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

class TareaNode(DjangoObjectType):
    class Meta:
        model = Tarea
        interfaces = (Node, )

class Query(ObjectType):
    tarea = Node.Field(TareaNode)
    all_tareas = DjangoConnectionField(TareaNode)