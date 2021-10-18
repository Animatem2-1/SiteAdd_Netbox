import csv

def mcreate(siteName, region, slug, facility, asn, contactPoint, dnsSiteName):
    status = "active"
    tenant = "ZHS"
    time_zone = "Europe/Warsaw"
    description = "Numer punktu kontaktowego " + contactPoint

    with open(r'C:\Users\A0715246\Music\Data_Netbox\netbox_sites.csv', 'a', newline='') as csvfile:
        fieldnames = ['name','slug','status','region','tenant','facility','asn','time_zone','description','physical_address','shipping_address','latitude','longitude','contact_name','contact_phone','contact_email','comments','cf_DNS Site Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


        writer.writerow({'name': siteName,'slug': slug,'status': status,'region': region,'tenant': tenant,'facility': facility,'asn': asn,'time_zone': time_zone,'description': description,'physical_address': '','shipping_address': '','latitude': '','longitude': '','contact_name': '','contact_phone': '','contact_email': '','comments': '','cf_DNS Site Name': dnsSiteName})
