import pandas as pd
import csv
data = []
with open("filtered_stars.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
planet_data = data[1:]
headers = data[0]
final_star_list = []
for data in planet_data:
    temp_dict = {
        "name":data[2],
        "distance":data[3],
        "mass":data[4],
        "radius":data[5],
        "gravity":data[6]
    }
    final_star_list.append(temp_dict)
print(final_star_list)