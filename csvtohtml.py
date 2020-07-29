import os
import time
import csv
from pathlib import Path

class CSVToHTML:
    # Get the projects directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the downloaded CSV files dir
    csv_dir = os.path.join(project_dir,"CSV_Files")

    def loop_through_csv_dir(self):
        csv_paths = [path for path in Path]

    def read_csv(self, input_file_name ,delimiter=","):
        """Read a CSV file"""
        with open(input_file_name, mode="r") as input_file:
            csv_file = csv.reader(input_file, encoding="utf-8", delimiter=delimiter)
            return csv_file

    def get_headings(self, **kwargs):
        csv_file = self.read_csv
        headers = csv_file[0]

    def loop_through_csv_dir(self):
        for file in os.listdir(self.csv_dir):
            return file
            csv_file = self.read_csv(file)
            csv_file_headings = self.get_headings(file)
            print(csv_file + "\n\n\n" + csv_file_headings)


csvtohtml = CSVToHTML()

csvtohtml.loop_through_csv_dir()

# TODO: figure out how to loop through the files in the directory and run the program on each file
