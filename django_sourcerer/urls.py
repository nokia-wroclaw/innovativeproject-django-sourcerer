from django.urls import include, path
from rest_framework import routers
from django_sourcerer import views

router = routers.DefaultRouter()
router.register(r'django_sourcerer', views.DjangoSourcerer)

urlpatterns = [
    path('', include(router.urls)),
]
