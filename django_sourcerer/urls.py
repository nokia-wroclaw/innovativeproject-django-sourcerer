from rest_framework import routers
from django_sourcerer import views


def django_sourcerer_urls():
    router = routers.DefaultRouter()
    router.register(r'django_sourcerer', views.DjangoSourcerer)
    return router
