def mcreate(siteName, region, slug, facility, asn, contactPoint, dnsSiteName):
    status = "active"
    tenant = "ZHS"
    time_zone = "Europe/Warsaw"
    description = "Numer punktu kontaktowego " + contactPoint
    fileAppend = open("netbox_sites.txt", "a")
    fileAppend.write("\r" + siteName +","+ slug +","+ status +","+ region + "," + tenant + "," + facility + "," + asn + "," + time_zone + "," + description + "," + dnsSiteName)
    fileAppend.close()
    #("name,slug,status,region,tenant,facility,asn,time_zone,description,DNS Site Name")
