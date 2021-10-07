from bs4 import BeautifulSoup
import requests
import json
link1="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
web1=requests.get(link1)
data1=web1.json
web3=BeautifulSoup(web1.text,"html.parser")
main_1=web3.find("div", class_="_1EI9").span.get_text()
# a=int(main_1[2:5])
# print(a)
# b=a//32+1
# print(b)
# a=main_1.split()
# print(a)
def web_pickel():
    web_pickel="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    web=requests.get(web_pickel)
    data=web.json
    web2=BeautifulSoup(web.text,"html.parser")
    main_div=web2.find("div", class_="_3RA-")
    main=main_div.find_all("div",class_="UGUy")
    main1=main_div.find_all("div",class_="_1kMS")
    # print(main1)
    main2=main_div.find_all("div",class_="_3WhJ")

    # print(main2)
    # print(main2)
    i=0
    list=[]
    while i<len(main):
        picals_name = main[i].get_text()
        picals_price=main1[i].span.get_text()
        pical_url="https://paytmmall.com"+main2[i].a["href"]
        i=i+1
    
        pical_det={"position":i,"picals_name":picals_name,"picals_price":picals_price,"pical_url":pical_url}
        pical_det["position"]=i
        list.append(pical_det)
        data1=web.json        
        with open("picckel_some details.json","w")as a:
            json.dump(list,a,indent=6)   
    return (list)
web_pickel()