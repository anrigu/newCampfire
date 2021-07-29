from django.core.management.base import BaseCommand, CommandError
import logging
import csv
import os

# Get an instance of a logger
# logger = logging.getLogger(_name_)


class Command(BaseCommand):
    help = 'Add category'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('input', type=str)
        parser.add_argument('output', type=str)

    def handle(self, *args, **options):
        path = os.path.join(os.getcwd(), "data",
                            options['input'])
        input_files = os.listdir(path)
        print(input_files)
        output_path = os.path.join(
            os.getcwd(), "data", options['output'])
        for file in input_files:
            self.process(file,path,output_path)

    def process(self, input_file, input_path, output_path):
        input = os.path.join(input_path,input_file)
        output = os.path.join(output_path,input_file)
        
        if os.path.exists(input):
            with open(input, 'r', newline='') as csvfile:
                with open(output, 'w', newline="", encoding="UTF-8") as output_csvfile:
                    line = csvfile.readline()
                    while line:
                        output_csvfile.write(line)
                        line = csvfile.readline()
        else:
            print("File doesn't exist", input)
