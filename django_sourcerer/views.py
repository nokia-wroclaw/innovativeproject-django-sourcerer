from django_sourcerer.models import AutoModels
from rest_framework import viewsets
from django_sourcerer.serializers import UserSerializer


class DjangoSourcerer(viewsets.ModelViewSet):
    queryset = AutoModels().use_model().objects.all()
    serializer_class = UserSerializer
