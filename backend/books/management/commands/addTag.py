from django.core.management.base import BaseCommand, CommandError
from books.models import Tag
import logging

class Command(BaseCommand):
    help = 'Add tag'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        self.create_tag(options['name'])
        
    def create_university(self, name):
      query = Tag.objects.filter(name=name)
      if len(query) == 0:
        print('Creating Tags')
        tag = Tag(name=name)
        tag.save()
      else:
        print("Already Exists.")
