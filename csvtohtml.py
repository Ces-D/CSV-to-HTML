import os
import time
import csv
from jinja2 import Environment, FileSystemLoader, select_autoescape
import webbrowser

project_dir = os.path.dirname(os.path.abspath(__file__))     # Get the projects directory
templates_dir = os.path.join(project_dir, "templates")       # Get the projects directory
env = Environment(loader=FileSystemLoader(templates_dir))

class CSVToHTML:
    def __init__(self, template= "example.html", header_pos= 0, delimeter= ","):
        self.csv_dir = os.path.join(project_dir, "CSV_Files")
        self.csv_file = None
        self.template = template
        self.delimeter = delimeter
        self.header_pos = header_pos

    def read_csv(self, csv_file_path):
        """Takes a given csv_file_path and returns the csv.reader object"""
        with open(csv_file_path, mode="r") as input_file:
            # return <_csv.reader object at 0x000001D2463D5820>
            read_csv = csv.reader(input_file, delimiter=self.delimeter)
            list_read_csv = []
            for row in read_csv:
                list_read_csv.append(row)
            self.csv_file = list_read_csv

    def get_headers_and_rows(self, csv_file_path):
        """Takes the csv render object and returns the headers and rows"""
        csv = self.read_csv(csv_file_path)

        csv_headers = [self.csv_file[self.header_pos]]

        csv_rows = [row for row in self.csv_file[self.header_pos+1:-1]]
        #print(csv_headers,"\n\n\n", csv_rows)
        return csv_headers, csv_rows

    def csv_to_html(self, csv_file_path):
        """Returns the formatted html table"""
        csv_headers, csv_rows = self.get_headers_and_rows(csv_file_path)
        data = {
            "headers": csv_headers,
            "rows": csv_rows
        }
        template = env.get_template(self.template)
        parsed_template = template.render(data)
        print(parsed_template)
        return parsed_template

    def save(self,csv_file_path):
        parsed_template = self.csv_to_html(csv_file_path)
        written_template=self.template
        with open(written_template,'w') as output_file:
            output_file.write(parsed_template)

    def loop_through_and_print(self):
        """Loops through the csv_files directory and returns the formatted html table"""
        with os.scandir(self.csv_dir) as input_file:
            for csv in input_file:
                if csv != None:
                    self.csv_file = csv
                    # function that actually converts to html
                    return self.csv_to_html
                else:
                    continue

    def loop_through_and_save(self):
        with os.scandir(self.csv_dir) as input_file:
            for csv in input_file:
                if csv != None:
                    self.csv_file = csv
                    # function that actually converts to html
                    return self.save(self.csv_file)
                else:
                    continue



csv_to_html = CSVToHTML(template="covid_resources_home.html", header_pos=4)
csv = csv_to_html.loop_through_and_save()

