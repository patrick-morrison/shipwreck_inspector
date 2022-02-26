from django.core.management.base import BaseCommand, CommandError
from wrecks.views import sites_csv, reports_csv, publications_csv, people_csv, photos_csv
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import datetime

class Command(BaseCommand):
    help = 'Saves CSV to Dropbox folder'

    def handle(self, *args, **options):
        try:
                now=datetime.datetime.now()
                date = now.strftime("%Y-%m-%d")

                contents = sites_csv('please').content
                filename = 'tables/sites-' + date + '.csv'
                default_storage.save(filename, ContentFile(contents))

                contents = reports_csv('please').content
                filename = 'tables/reports-' + date + '.csv'
                default_storage.save(filename, ContentFile(contents))

                contents = publications_csv('please').content
                filename = 'tables/publications-' + date + '.csv'
                default_storage.save(filename, ContentFile(contents))

                contents = people_csv('please').content
                filename = 'tables/people-' + date + '.csv'
                default_storage.save(filename, ContentFile(contents))

                contents = photos_csv('please').content
                filename = 'tables/photos-' + date + '.csv'
                default_storage.save(filename, ContentFile(contents))

                contents = projects_csv('please').content
                filename = 'tables/projects-' + date + '.csv'
                default_storage.save(filename, ContentFile(contents))
        except:
            self.stdout.write(self.style.ERROR('Save failed.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully saved csv files'))
        return