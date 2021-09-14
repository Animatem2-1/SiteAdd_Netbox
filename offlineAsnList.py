import checkUsedNetboxRegions
import sys
import json


def offlineAsnList():

    with open("oldAsnBase.txt") as a:
        strDict = a.read()
    strDict = strDict.replace("'", '"')
    oldAsnBase = json.loads(strDict)


    tempAsnBase = checkUsedNetboxRegions.netboxBaseASN()


    if oldAsnBase == tempAsnBase:
        print("Zgodne!")
    else: print("Niezgodnosc! Zaaktualizuj stara baze.")


    with open("actualAsnBase.txt") as f:
        data = f.read()
    data = data.replace("'", '"')
    actualAsnBase = json.loads(data)

    return actualAsnBase
