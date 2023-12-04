# Inside myapp/management/commands/my_custom_command.py

from django.core.management.base import BaseCommand
from api.models import Vendor , PurchasedOrder , HistoricalPerformance
import datetime

class Command(BaseCommand):
    help = 'This is a command file which stores records of vendor on daily basis'

    def handle(self, *args, **kwargs):
        all_vendors = list(Vendor.objects.values_list("id", flat=True))
        all_vendors = Vendor.objects.all()

        for i in all_vendors:
            history_obj = HistoricalPerformance()
            id= i.id
            on_time_delivery_rate = i.on_time_delivery_rate
            quality_rating_avg = i.quality_rating_avg
            average_response_time = i.average_response_time
            fulfillment_rate = i.fulfillment_rate
            today = datetime.date.today()
            history_obj.date = today
            history_obj.on_time_delivery_rate = on_time_delivery_rate
            history_obj.average_response_time = average_response_time
            history_obj.fulfillment_rate=fulfillment_rate
            history_obj.vendor = i
            history_obj.quality_rating_avg=quality_rating_avg
            history_obj.save()
