from django.core.management.base import BaseCommand, CommandError
from books.models import Book, Tag, Author
#from profile.university_models import University
import logging
import csv
import os

# Get an instance of a logger
# logger = logging.getLogger(_name_)


class Command(BaseCommand):
    help = 'Add category'

    def capitalize(self,title):
        title_split = title.split()
        for i in range(0,len(title_split)):
            title_split[i] = title_split[i].capitalize()
        return " ".join(title_split)

#    def add_arguments(self, parser):
        # Positional arguments
        # #parser.add_argument('prefix', type=str)

    def handle(self, *args, **options):
        self.load_csv()
        #self.delete_all_tags()

    def fix_nulls(self, s):
        for line in s:
            yield line.replace('\0', '')
    
    def load_csv(self):
        path = os.path.join(os.getcwd(), "data", "raw", "init.csv")
        if os.path.exists(path):
            with open(path, newline='') as csvfile:
                tag_reader = csv.reader(
                    self.fix_nulls(csvfile), delimiter=',')
                for row in tag_reader:
                    if len(row) >= 1:
                        author = row[1].split()
                        tags = row[-1].split("; ")
                        self.create_book(self.capitalize(row[0]), author[0], " ".join(author[1:len(author)]),row[3], row[2], tags)
        else:
            print("File doesn't exist")
    
    def create_author(self, first_name, last_name):
        author = Author(first_name = first_name, last_name = last_name)
        author.save()  
        return author

    def create_book(self, name, author_first, author_last, publication_year, edition, tags_name_list):
        queryBook = Book.objects.filter(title=name) #add more later
        #print(queryBook)
        if (len(queryBook) == 0):
            queryAuthor = Author.objects.filter(first_name = author_first, last_name = author_last)
            tags_list = self.process_tags(tags_name_list)
            if (len(queryAuthor) == 0):
                author = self.create_author(author_first, author_last)
                book = Book(title=name, author=author, publishing_year=publication_year, edition = edition)
            else:
                book = Book(title=name, author=queryAuthor[0], publishing_year=publication_year, edition = edition)
            print("book create", book.title)
            book.save()
            for tag in tags_list:
                book.tags.add(tag)
            
        else:
            print("Book already exist" + name)
    
    def process_tags(self, name_list):
        tags_list = []
        for name in name_list:
            queryTag = Tag.objects.filter(name=name)
            if (len(queryTag) == 0):
                tag = self.create_tag(name)
                tags_list.append(tag)
            else:
                tags_list.append(queryTag[0])
        print("tags_list",tags_list)
        return tags_list

    def create_tag(self, name):
        queryTag = Tag.objects.filter(name = name)
        if (len(queryTag) == 0):
            tag = Tag(name = name)
            tag.save()
        else:
            print("Tag already exists" + name)
        return tag
    
    def delete_all_tags(self):
        query = Tag.objects.all().delete()
        query = Author.objects.all().delete()
        query = Book.objects.all().delete()
    #   query = University.objects.filter(name=options['name'])
    #   if len(query) == 0:
    #     logger.info('Creating a new University')
    #     univ = University(name=options['name'])
    #     univ.save()
    #   else:
    #     logger.info('Already exists')
