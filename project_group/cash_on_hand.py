from pathlib import Path
import re, csv


file_path = Path.cwd()/"project_group"/"csv_reports"/"Cash_On_Hand.CSV"
print(file_path.exists())

for file in file_path.open():
         empty_list = []
         with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
              reader = file.read()
              
              