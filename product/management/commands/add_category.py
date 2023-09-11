from django.core.management.base import BaseCommand
from product.models import Category


class Command(BaseCommand):
    # help = 'To add these categories 1] Electrical Appliances, 2] Clothes, 3] Home Appliances, 4] Footwares'

    def handle(self, *args, **kwargs):

        categories = [
            'Electrical Appliances',
            'Clothes',
            'Home Appliances',
            'Footwares'
            ]

        for category in categories:
            Category.objects.create(name=category)
