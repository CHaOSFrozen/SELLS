from pathlib import Path
import re, csv


file_path = Path.cwd()/"project_group"/"csv_reports"/"Cash On Hand.CSV"
print(file_path.exists())

for file in file_path.open():
         empty_list = []
         with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
             # instantiate a read object
              reader = file.read()
              # use `next()` to skip the header.
              next(reader)
              