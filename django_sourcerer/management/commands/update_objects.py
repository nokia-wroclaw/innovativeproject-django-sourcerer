from django.core.management.base import BaseCommand

from django_sourcerer.import_datas.intermediate_layer import Adapter
from django_sourcerer.models import AutoModels


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        instance = AutoModels().use_model()
        records = Adapter().get_df()
        for i in records:
            to_db = [instance(**i)]
            instance.objects.bulk_create(to_db)
