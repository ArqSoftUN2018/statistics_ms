import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from estadisticas.models import Estadistica

class EstadisticaNode(DjangoObjectType):
    class Meta:
        model = Estadistica
        filter_fields = {
            'nombre': ['exact','istartswith'],
	        'creado_por': ['exact','istartswith'],
	        'fecha_creacion': ['exact'],
    	    'tipo_reporte': ['exact','istartswith'],
        }
        interfaces = (relay.Node, )

class Query(ObjectType):

    estadisticas = relay.Node.Field(EstadisticaNode)
    all_estadisticas = DjangoFilterConnectionField(EstadisticaNode)

    def resolve_estadisticas(self):
        return Estadistica.objects.all()

schema = graphene.Schema(query=Query,)