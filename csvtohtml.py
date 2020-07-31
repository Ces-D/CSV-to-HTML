import os
import time
import csv
from jinja2 import Environment, PackageLoader, select_autoescape


class CSVToHTML:
    def __init__(self,template_name):
        self.project_dir = os.path.dirname(os.path.abspath(__file__))       # Get the projects directory
        self.csv_dir = os.path.join(self.project_dir,"CSV_Files")           # Get the downloaded CSV files dir
        self.csv_file = None                                                # CSV file is empty until read                
        self.templates_dir = os.path.join(self.project_dir,"templates")
        self.template = template_name
    
    def set_jinja(self):
        """Creates the jinja environment and renders the template chosen"""
        env = Environment(
            loader=FileSystemLoader(self.templates_dir),
            autoescape=select_autoescape(["html", "xml", "j2"])
        )
        template = env.get_template(self.template)


    def read_csv(self, csv_file_path):
        """Takes a given csv_file_path and returns the csv.reader object"""
        with open(input_file_path, mode="rb") as input_file:
            self.csv_file = csv.reader(input_file) # return <_csv.reader object at 0x000001D2463D5820>

    def get_csv_items(self):
        """Takes the read csv file and appends each row to list, all_csv_rows. Returns all_csv_rows. Requires header always be present"""
        csv_object = self.csv_file  # created in read_csv()
        all_csv_rows = []
        for row in csv_object:
            all_csv_rows += row
        return all_csv_rows
    
    def get_headers(self):
        """Takes list of csv items and extracts first row aka list containing headers. Return headers"""
        all_csv_rows = self.get_csv_items() # list of all_csv_rows
        headers = all_csv_rows[0]
        return headers


    def convert_to_html(self, csv):
        """Should take in a csv file path and run all self.functions. Return converted csv to html template """
        caption = kwargs.get("caption") or "Table"
        display_length = kwargs.get("display_length") or -1
        height = kwargs.get("height") or "70vh"

        default_length_menu = [-1, 10, 25, 50]
        pagination = options.get("pagination")
        virtual_scroll_limit = options.get("virtual_scroll")

        # Change % to vh
        height = height.replace("%", "vh")

        # Header columns
        columns = []
        for header in table_headers:
            columns.append({"title": header})

        # Data table options
        datatable_options = {
            "columns": columns,
            "data": table_items,
            "iDisplayLength": display_length,
            "sScrollX": "100%",
            "sScrollXInner": "100%"
        }
        return template(datatable_options)

    def loop_through_csv_files(self):
        with os.scandir(self.csv_dir) as input_file:
            for csv in input_file:
                if csv != None:
                    return convert_to_html(csv) # function that actually converts to html
                else:
                    continue
    

csv_to_html = CSVToHTML()
csv = csv_to_html.loop_through_csv_files()
print(csv)

