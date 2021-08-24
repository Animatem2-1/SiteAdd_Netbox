import sys
import json
import oncsvRegions
import oncsvSites
import fileCreator
#Poczatek - generowanie bazy lub nie

print("Generowanie bazy...")
try:
    file = open("netbox_sites.txt", "x") #x nie doda pliku, gdy juz istnieje
    file.write("name,slug,status,region,tenant,facility,asn,time_zone,description,cf_DNS Site Name")
    file.close()
except:
    print("Plik istnieje. Wygenerowac nowy? (y/n)")
    newFileBoolean = input()
    if newFileBoolean == "y":
        file = open("netbox_sites.txt", "w") #w nadpisze dokument
        file.write("name,slug,status,region,tenant,facility,asn,time_zone,description,cf_DNS Site Name")
        file.close()
    else: pass

#Koniec generowania bazy

print("Wprowadz nazwe site'u:")
siteName = input()
print("Wprowadz akronim regionu lub wpisz help, aby wyswietlic dostepne regiony:")
region = input()
if region == "help":
    oncsvRegions.mcsvfile()
    print("Wprowdz akronim regionu:")
    region = input()
slug = siteName.lower().replace(" ", "-") # slug generator
print("Wprowadz numer obiektu:")
facility = input()
asn = str(oncsvSites.mASNno(region))
print("Generowanie ostatniego zarejestrowanego ASN...")
print("Wynik: " + asn)
print("Wprowadz kolejny numer ASN:")
asn = input()
print("Wprowadz numer punktu kontaktowego:")
contactPoint = input()
print("Wprowadz DNS Site Name (drugi oktet nazwy urzadzenia):")
dnsSiteName = input()
fileCreator.mcreate(siteName, region, slug, facility, asn, contactPoint, dnsSiteName)
