from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    help = "Creates the periodic task to import orders"

    def handle(self, *args, **kwargs):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=5,
            period=IntervalSchedule.MINUTES,
        )

        task, created = PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="Import orders automatically",
            task="src.orders.tasks.import_orders",
            defaults={"args": json.dumps([])},
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Task created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("The task already existed!"))
