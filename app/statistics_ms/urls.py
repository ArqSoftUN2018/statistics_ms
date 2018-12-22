"""statistics_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from upload.views import image_upload
from graphene_django.views import GraphQLView
schema_view = get_swagger_view(title='Statistics API')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    path('', image_upload, name='upload'),
    url(r'^', include('reportes.urls')),
    url(r'^', include('tareas.urls')),
    url(r'^', include('estadisticas.urls')),
    url(r'^$', schema_view),
]
