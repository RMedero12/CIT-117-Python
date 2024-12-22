#Ricardo Medero



import csv

#FUNTION TO GET DATA FROM THE CSV FILE AND PAST TO LIST RECORD THEM RETURN RECORD TO MAIN FUCTION
def getDataInput(sFileName:str):
    with open(sFileName, "r") as file:
        records = []
        reader = csv.reader(file)
        listHeader = next(reader)
        for row in reader:
            records.append(row)
        return (records)
#FUNTION TO GET THE MEDIAN
def getMedian(Med, lstPrices):
    if Med % 2 == 0:
        Median1 = lstPrices[Med//2]
        Median2 = lstPrices[Med // 2 - 1]
        Median = (Median1 + Median2)/2
        return Median
    else:
        Median = lstPrices[Med//2]
        return Median

#DEF MAIN WERE EVERITHING START AND RECIVED HE DATA WITH LIST AND DICTIONARY

def main():

    Records = getDataInput("RealEstateData.csv")
    listCitys = []
    listPropertyTypes =[]
    listPrices = []
    dictCitys = {}
    dictZips = {}
    dictPropertyTypes = {}
#FOR LOOP TO GET THE DATA IN ROW CITY,ZIPCODE,PROPETYTYPE AND PRICEL.
    for row in Records:

        sCity = row[1]
        sZip = row[2]
        sPropertyType = row[7]
        fPrice = float(row[8])
#CONDITION IF THE CITY IS NOT ON LIST WILL ADD TO THE LIST  AND MAKE LOGIC
        if sCity not in listCitys:
            listCitys.append(sCity)
        if sPropertyType not in listPropertyTypes:
            listPropertyTypes.append(sPropertyType)
        listPrices.append(fPrice)
        dictCitys[sCity] = dictCitys.get(sCity, 0) + fPrice
        dictZips[sZip] = dictZips.get(sZip, 0) + fPrice
        dictPropertyTypes[sPropertyType] = dictPropertyTypes.get(sPropertyType, 0) + fPrice
#WILL SORT THE LSIT AND THEN GET THE MEDIAN DATA
    listPrices.sort()
    Med = len(listPrices)
    Median = getMedian(Med, listPrices)

#OUTPUT AND FOR LOOP TO OUTPUT PROPERTY TYPE AND CITY
    print(f"\n{'Minimum':16}{min(listPrices):16,.2f}")
    print(f"{'Maximum':16}{max(listPrices):16,.2f}")
    print(f"{'Sum':16}{sum(listPrices):16,.2f}")
    print(f"{'Avg':16}{sum(listPrices) / len(listPrices):16,.2f}")
    print(f"{'Median':16}{Median:16,.2f}")

    print("\nTotal Prices by Property Type:\n"
          "----------------------------------")
    for Property_Type, Total in dictPropertyTypes.items():
        print(f"{Property_Type:16} {Total:16,.2f}")


    print("\nSummary by City:\n"
          "----------------------------------")
    for City, Total in dictCitys.items():
        print(f"{City:16} {Total:16,.2f}")




main()