import sys
import json
import getRegAsn
import fileCreator


print("Wprowadz nazwe site'u:")
siteName = input()
print("Wprowadz akronim regionu lub wpisz help, aby wyswietlic dostepne regiony:")
region = input()
if region == "help":
    asnDict = getRegAsn.getRegAsn()
    for x in asnDict.keys():
        print(x)
    print("Wprowadz akronim regionu:")
    region = input()
slug = siteName.lower().replace(" ", "-") # slug generator
print("Wprowadz numer obiektu:")
facility = input()

dictRegAsn = getRegAsn.getRegAsn()
asn = str(dictRegAsn[region])

print("Generowanie ostatniego zarejestrowanego ASN...")
print("Wynik: " + asn)
print("Wprowadz kolejny numer ASN:")
asn = input()
print("Wprowadz numer punktu kontaktowego:")
contactPoint = input()
print("Wprowadz DNS Site Name (drugi oktet nazwy urzadzenia):")
dnsSiteName = input()

fileCreator.mcreate(siteName, region, slug, facility, asn, contactPoint, dnsSiteName)
