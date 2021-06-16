import csv

bright_stars = []
dwarf_stars = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader: 
        bright_stars.append(i)

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader: 
        dwarf_stars.append(i)

header1 = bright_stars[0]
bright_stars_data = bright_stars[1:]

header2 = dwarf_stars[0]
dwarf_stars_data = dwarf_stars[1:]

headers = header1 + header2

star_data = []

for index, data_row in enumerate(bright_stars_data):
    star_data.append(bright_stars_data[index] + dwarf_stars_data[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)