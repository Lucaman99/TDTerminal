import json
import pandas as pd

df = pd.DataFrame()

y = json.loads(open("transaction.json").read())

print(len(y.keys()))

df["id"] = pd.Series(y.keys())

city = []
merchantCategoryCode = []
merchantName = []
longitude = []
amount = []
latitude = []

for i in y.keys():
    city.append(y[i]["city"])
    merchantCategoryCode.append(y[i]["merchantCategoryCode"])
    merchantName.append(y[i]["merchantName"])
    longitude.append(y[i]["longitude"])
    amount.append(y[i]["amount"])
    latitude.append(y[i]["latitude"])

df["city"] = pd.Series(city)
df["merchantCategoryCode"] = pd.Series(merchantCategoryCode)
df["merchantName"] = pd.Series(merchantName)
df["longitude"] = pd.Series(longitude)
df["currencyAmount"] = pd.Series(amount)
df["latitude"] = pd.Series(latitude)

df.to_csv("out.csv")
