from django_sourcerer.models import AutoModels
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoModels().use_model()
        fields = '__all__'
