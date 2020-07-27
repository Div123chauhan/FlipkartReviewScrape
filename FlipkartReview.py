# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:29:34 2020

@author: parkar
"""


import bs4
import requests
import pandas as pd
import csv
res=requests.get("https://www.flipkart.com/samsung-galaxy-m01-blue-32-gb/product-reviews/itmc068b26305a0d?pid=MOBFRZZHMHQVNDFA&lid=LSTMOBFRZZHMHQVNDFAO0E4YL&marketplace=FLIPKART")
soup=bs4.BeautifulSoup(res.text,"lxml")
title=soup.select("._2xg6Ul")
review=soup.select(".qwjRop")
rating=soup.select(".hGSR34")
name=soup.select("._3sxSiS")
details=pd.DataFrame.columns=('Title','Review','Rating',"Reviewer_name")
l=0

with open('FlipkartReview.csv', 'w', newline='') as file:
    c = csv.writer(file)
    c.writerow(['Title','Review','Rating','Reviewer_name'])
for i,j,k,n in zip(title,review,rating,name):
    with open('FlipkartReview.csv', 'a', newline='',encoding='UTF-8') as file:
        c = csv.writer(file)
        c.writerow([i.text, j.text,k.text,n.text])