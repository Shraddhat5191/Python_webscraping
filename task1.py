from os import PRIO_PGRP
from bs4 import BeautifulSoup
import requests
import json
import pprint

def scrape_top_list():
    url="https://www.imdb.com/india/top-rated-indian-movies/?ref =nv mv 250 in"
    page=requests.get(url)
    data1=page.json
    code=BeautifulSoup(page.text,"html.parser")
    main_div=code.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    movie_=tbody.find_all("td",class_="titleColumn")
    a=tbody.find_all("tr")
    movie=[]
    j=0
    for i in a:   
        j=j+1
        name=i.find("td",class_="titleColumn").a.get_text()
        year=i.find("td",class_="titleColumn").span.get_text()
        movie_year=year[1:5]                               
        rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        link=i.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_detaile={"position":"","name":"","year":"","rating":"","movie_link":""}
        movie_detaile["position"]=j
        movie_detaile["name"]=name
        movie_detaile["year"]=int(movie_year)
        movie_detaile["rating"]=float(rating)
        movie_detaile["movie_link"]=movie_link
        movie.append(movie_detaile)       
        with open("imdbtask1.json","w")as a:
            json.dump(movie,a,indent=6)   
    return (movie)
scrape_top_list()  