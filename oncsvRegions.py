import csv
import re

def mcsvfile():
    with open("netbox_regions.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if re.match('^2..', row['description']) :
                print(row['name'])
            else:
                pass
