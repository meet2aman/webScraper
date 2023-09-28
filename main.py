import requests
from bs4 import BeautifulSoup
import pandas as pa


product_name = []
prices = []
descs = []
rvs = []
offers = []


for i in range(2, 8):
    url = "https://www.flipkart.com/search?q=mobile+phones+under+20k&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_20_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_20_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mobile+phones+under+20k&requestId=f482e27b-03ca-4445-8ccc-3b3f63c10b5d&as-searchtext=mobile+phones+under+&page=" + \
        str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    # print(names)

    # ------------------   for Prodect Name -------------------
    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        names = i.text
        product_name.append(names)
    # print(len(product_name))

    # ------------------   for prices -------------------

    price = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in price:
        names = i.text
        prices.append(names)
    # print(len(prices))

    # ------------------   for Decs -------------------
    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        names = i.text
        descs.append(names)
    # print(len(descs))

    # ------------------   for reviews -------------------
    reviews = box.find_all("div", class_="_3LWZlK")
    for i in reviews:
        names = i.text
        rvs.append(names)
    # print(len(rvs))

    # ------------------ Extras  -------------------

    # print(soup)
    # while True:
    # np = soup.find("a", class_="_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com" + np
    # print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, "lxml")


df = pa.DataFrame({"Prodect Name": product_name,
                  "Prices": prices, "Description": descs, "Reviews": rvs})
# print(df)
df.to_csv("/Users/amankushwaha/Desktop/flipkart_under_20k.csv")
