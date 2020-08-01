import os
import time
import csv
from jinja2 import Environment, FileSystemLoader, select_autoescape


class CSVToHTML:
    def __init__(self, template_name="CSV-to-Html"):
        self.project_dir = os.path.dirname(os.path.abspath(__file__))       # Get the projects directory
        self.csv_dir = os.path.join(self.project_dir, "CSV_Files")
        self.csv_file = None
        self.templates_dir = os.path.join(self.project_dir, "templates")
        self.template_name = template_name

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
        csv = self.read_csv(csv_file_path)

        csv_headers = [self.csv_file[0]]

        csv_rows = [row for row in self.csv_file[1:-1]]
        #print(csv_headers,"\n\n\n", csv_rows)
        return csv_headers, csv_rows

    def write_to_html(self):
        i = 1 
        csv_headers, csv_rows = self.get_headers_and_rows()
        new_html = self.templates_dir + self.template_name + ".html"
        f = open(new_html,'w')
        f.write('<html><head>' + self.template_name + '</head><body><table>')
        for row in csv_rows:
            print (each)
            f.write('<tr><td><b>')
            f.write(b[j]+':')
            f.write('</b></td><td>')
            f.write(each)
            f.write('</td></tr>')
            f.write('\n')
            print('/n')
            j+=1
        f.write('</table></body><html>')
        f.close()

        for header in csv_headers:
            f.write("<thead>")
        for row in csv_rows:
            f.write(thead)



    def loop_through_csv_files(self):
        with os.scandir(self.csv_dir) as input_file:
            for csv in input_file:
                if csv != None:
                    # function that actually converts to html
                    return self.get_headers_and_rows(csv)
                else:
                    continue


csv_to_html = CSVToHTML()
csv = csv_to_html.loop_through_csv_files()

