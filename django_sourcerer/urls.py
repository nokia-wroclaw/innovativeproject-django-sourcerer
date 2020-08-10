from rest_framework import routers

from django_sourcerer import views
from django_sourcerer.import_datas.intermediate_layer import Adapter


def django_sourcerer_urls():
    route_name = Adapter().model_name()
    router = routers.DefaultRouter()
    router.register(r'{}'.format(route_name), views.DjangoSourcerer)
    return router
