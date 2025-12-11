import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    help = "Import phones from CSV"

    def handle(self, *args, **options):
        with open('phones.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'price': float(row['price']),
                        'image': row['image'],
                        'release_date': row['release_date'],
                        'lte_exists': row['lte_exists'].lower() == 'true',
                        'slug': slugify(row['name']),
                    }
                )

        self.stdout.write(self.style.SUCCESS("Импорт завершен"))
