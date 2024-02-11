from django.core.management.base import BaseCommand, CommandError
from phones.models import Phone
import csv
from django.template.defaultfilters import slugify


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter = ";")
            next(file_reader)
            for row in file_reader:
                new_phone = Phone.objects.create(
                    id=int(row[0]), 
                    name=row[1],
                    price=int(row[3]), 
                    image=row[2],
                    release_date=row[4],
                    lte_exist=row[5],
                    slug=slugify(row[1]),
                )
