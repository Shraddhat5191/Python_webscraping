from bs4 import BeautifulSoup
import requests
import json
import pprint
def web_pical():
    link1="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    shr=requests.get(link1)
    # data1=shr.json
    shra=BeautifulSoup(shr.text,"html.parser")
    main_1=shra.find("div", class_="_1gX7").span.get_text()
    print(main_1)
    div=main_1.split()
    a=int(div[1])
    b=a//32+1
    print(b)
    s=0
    posi=1
    list1=[]
    while s<=b:
        web_pickel="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(s)
        web=requests.get(web_pickel)
        web2=BeautifulSoup(web.text,"html.parser")
        main_div=web2.find("div", class_="_3RA-")
        main=main_div.find_all("div",class_="UGUy")
        main1=main_div.find_all("div",class_="_1kMS")
        main2=main_div.find_all("div",class_="_3WhJ")
        i=0
        while i<len(main):
            picals_name = main[i].get_text()
            # print(picals_name)
            picals_price=main1[i].span.get_text()
            pical_url="https://paytmmall.com"+main2[i].a["href"]
            # print(pical_url)
            pical_det={"position":i+1,"picals_name":picals_name,"picals_price":picals_price,"pical_url":pical_url}
            list1.append(pical_det.copy())
            i=i+1
        # posi=posi+i
        s=s+1     
    with open("picals_all details.json","w") as f:
        json.dump(list1,f,indent=4)
    return list1    
web_pical()