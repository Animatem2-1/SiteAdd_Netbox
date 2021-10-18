import csv
import re

def getRegAsn():
    dictRegAsn = {}
    with open(r"C:\Users\A0715246\Music\Data_Netbox\netbox_regions.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if re.match('^2..', row['description']) :
                dictRegAsn[row['name']] = 0
            else:
                pass
    csvfile.close()


    with open(r"C:\Users\A0715246\Music\Data_Netbox\netbox_sites.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['region'] in dictRegAsn:
                x = dictRegAsn.get(row['region'])
                x += 1
                dictRegAsn[row['region']] = x
    csvfile.close()
    return dictRegAsn
