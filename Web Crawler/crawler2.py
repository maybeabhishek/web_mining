import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import sys

num = sys.argv[1]
word = sys.argv[2]
site = sys.argv[3]

response = requests.get(site)

soup = BeautifulSoup(response.text, "html.parser")
count = 0
for a in soup.findAll('a'):
    if(count+1==int(num)):
        break
    curr_url = a["href"]
    if(re.search("htt",curr_url) and curr_url != "http://intranet.vit.ac.in"):
        res = requests.get(curr_url)
        count=count+1
        print(count,"     ",curr_url)
    else:
        continue
    curr_soup = BeautifulSoup(res.text, "html.parser")
    for text in curr_soup.findAll('body'):  
        if re.search(word,text.text.lower()):
            print("\n\nFound word ",word," in : ",a["href"],"\n\n")
            break

