import os
import time
import csv
from jinja2 import Environment, FileSystemLoader, select_autoescape
import webbrowser

project_dir = os.path.dirname(os.path.abspath(__file__))     # Get the projects directory
templates_dir = os.path.join(project_dir, "templates")       # Get the projects directory
env = Environment(loader=FileSystemLoader(templates_dir))

class CSVToHTML:
    def __init__(self, template="qedc_table.html"):
        self.csv_dir = os.path.join(project_dir, "CSV_Files")
        self.csv_file = None
        self.template = template

    def read_csv(self, csv_file_path):
        """Takes a given csv_file_path and returns the csv.reader object"""
        with open(csv_file_path, mode="r") as input_file:
            # return <_csv.reader object at 0x000001D2463D5820>
            read_csv = csv.reader(input_file, delimiter=",")
            list_read_csv = []
            for row in read_csv:
                list_read_csv.append(row)
            self.csv_file = list_read_csv

    def get_headers_and_rows(self, csv_file_path):
        """Takes the csv render object and returns the headers and rows"""
        csv = self.read_csv(csv_file_path)

        csv_headers = [self.csv_file[0]]

        csv_rows = [row for row in self.csv_file[1:-1]]
        #print(csv_headers,"\n\n\n", csv_rows)
        return csv_headers, csv_rows


    def csv_to_html(self, csv_file_path):
        """Returns the formatted html table"""
        csv = self.get_headers_and_rows(csv_file_path)
        csv_headers, csv_rows = csv[0], csv[1]
        data = {
            "headers": csv_headers,
            "rows": csv_rows
        }
        template = env.get_template(self.template)
        parsed_template = template.render(data)
        print(parsed_template)


    def loop_through_csv_files(self):
        """Loops through the csv_files directory and returns the formatted html table"""
        with os.scandir(self.csv_dir) as input_file:
            for csv in input_file:
                if csv != None:
                    # function that actually converts to html
                    return self.csv_to_html(csv)
                else:
                    continue


csv_to_html = CSVToHTML()
csv = csv_to_html.loop_through_csv_files()
