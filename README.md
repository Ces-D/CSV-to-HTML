# CSV-to-HTML
Convert downloaded CSV files to HTML webpages. 

## Problem
Many small companies do not have the know-how or the resources to update their websites constantly. In these conditions, free collaborative products such as google sheets and docs become the go to tools for creating content. The issue arrives when translating this content into HTML for their webpages. They need simple but powerful tools, that specialize in specific jobs. 

## Solution
CSV-to-HTML requires the user to download the finished Google Sheet as a CSV, upload it and watch as it gets transformed into HTML that they can then upload to their websites. This is especially useful for CMS such as WordPress. 

## Use
Step 1 - Place your csv files in "CSV_Files" directory
Step 1 - Look at the "example.html" file found in "templates" directory for an example of how to format your Jinja2 syntax
Step 2 - Create your html template, saving it in the "templates" directory
Step 3 - When initializing the class, pass the name of your template as a value(template="example.html")
Step 4 - Run your file CSVtoHTML.loop_through_csv_files()

### References:
https://github.com/vividvilla/csvtotable
https://github.com/derekeder/csv-to-html-table
https://github.com/yeskarthik/CSV-to-HTML-report-generator/blob/master/csvtohtmls.py
https://www.youtube.com/watch?v=lhpNRDGzInw