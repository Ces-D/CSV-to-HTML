# CSV-to-HTML
Convert downloaded CSV files to HTML webpages. 

---

## Problem
Many small companies do not have the know-how or the resources to update their websites constantly. In these conditions, free collaborative products such as google sheets and docs become the go to tools for creating content. The issue arrives when translating this content into HTML for their webpages. They need simple but powerful tools, that specialize in specific jobs. 

***

## Solution
CSV-to-HTML requires the user to download the finished Google Sheet as a CSV, upload it and watch as it gets transformed into HTML that they can then upload to their websites. This is especially useful for CMS such as WordPress. 

---

## Setup
1. Place your csv files in "CSV_Files" directory 
2. Using the "example.html" template as a guide, create your personalized Jinja2 template or use the "example.html" template
3. When initializing the class, pass the name of your template as a value(template="example.html")
4. Run your file as either CSVToHTML.loop_through_and_save() or CSVToHTML.loop_through_and_print() 

***

```
class CSVToHTML:
    def __init__(self, template= "example.html", header_pos= 0, delimiter= ","):
```

### References:
https://github.com/vividvilla/csvtotable
https://github.com/derekeder/csv-to-html-table
https://github.com/yeskarthik/CSV-to-HTML-report-generator/blob/master/csvtohtmls.py
https://www.youtube.com/watch?v=lhpNRDGzInw
