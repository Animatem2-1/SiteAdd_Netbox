import offlineAsnList
import sys
import json

def upgrading(region, asn):
    with open("actualAsnBase.txt") as f:
        data = f.read()
    data = data.replace("'", '"')
    actualAsnBase = json.loads(data)
    actualAsnBase.update({region: asn})
    file = open("actualAsnBase.txt", "w")
    file.write(str(actualAsnBase))
    file.close()
