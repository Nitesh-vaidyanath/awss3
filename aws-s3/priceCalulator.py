import json 

def priceEstimation(bucketInfo):
    with open("./pricing.json", "rb") as e:
         priceFile = e.read()
         priceJson = json.loads(priceFile)
         for key in bucketInfo.iterkeys():
                 region = bucketInfo[key]["region"]
                 size =  (float(bucketInfo[key]["size"]))/(1024*1024*1024*1024)
                 size50 = size - 50
                 if size50 <= 0:
                    price = size * 1024 * priceJson["region"][region]["50"]
                 elif size50 > 0 and size50 <= 450:
                    price50 = 50 * 1024 * priceJson["region"][region]["50"]
                    price450 = size50 * 1024 *  priceJson["region"][region]["450"]
                    price = price50 + price450
                 else:
                    price50 = 50 * 1024 * priceJson["region"][region]["50"]
                    price450 = 450 * 1024 *  priceJson["region"][region]["450"]
                    price500 = (size50 - 450) * 1024 *  priceJson["region"][region]["500"]
                    price = price50 + price450 + price500
                 bucketInfo[key]["EstimatedPrice"] = price
         return  bucketInfo

