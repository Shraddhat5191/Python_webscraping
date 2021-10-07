from bs4 import BeautifulSoup
import requests
import os
import json
def web_event():
    if os.path.isfile("courses.json"):
        with open("courses.json","r") as saral:
            new_data= json.load(saral)
        # new_data=json.load(saral)
    else:
        E_Commerce_api = "https://webscraper.io/test-sites"
        E_Commerce_url = requests.get(E_Commerce_api)
        web_commerce_data = E_Commerce_url.json
        code = BeautifulSoup(E_Commerce_url.text,'html.parser')
        main_div=code.find("div",class_="container test-sites")
        main=main_div.find_all("h2")
        list1=[]
        j=1
        for i in main:
            a=(i.get_text().strip())
            b=("https://webscraper.io"+i.a["href"])
            dict1={"position":j,"name":a,"url":b}
            j+=1
            list1.append(dict1)
            with open("E_Commerce.json","w")as a:
                json.dump(list1,a,indent=3)
        return list1
web_event()