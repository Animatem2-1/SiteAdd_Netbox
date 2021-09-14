import csv
import re

def netboxBaseASN():
    dictRegion = {}
    with open("netbox_regions.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if re.match('^2..', row['description']) :
                dictRegion[row['name']] = 0
            else:
                pass
    csvfile.close()


    with open("netbox_sites.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['region'] in dictRegion:
                x = dictRegion.get(row['region'])
                x += 1
                dictRegion[row['region']] = x
    csvfile.close()
    return dictRegion
