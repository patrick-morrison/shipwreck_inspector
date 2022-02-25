from django.core.management.base import BaseCommand, CommandError
from wrecks.models import Site

class Command(BaseCommand):
    help = 'Saves all sites to make slugs'

    def handle(self, *args, **options):
        try:
            for s in Site.objects.all():
                s.save()
        except:
            self.stdout.write(self.style.ERROR('Save failed.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully saved all sites'))
        return