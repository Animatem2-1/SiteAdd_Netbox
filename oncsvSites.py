import csv
import re

def mASNno(region):
    with open("netbox_sites.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        highestNo = 0
        for row in reader:
            if re.match(region, row['region']):
                highestNo += 1
            else:pass
        return highestNo
