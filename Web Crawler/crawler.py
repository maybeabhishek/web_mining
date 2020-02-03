import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

url = "http://vit.ac.in"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
for a in soup.findAll('a'):
    curr_url = a["href"]
    # print(curr_url)
    if(re.search("htt",curr_url) and curr_url != "http://intranet.vit.ac.in"):
        res = requests.get(curr_url)
    else:
        continue
    curr_soup = BeautifulSoup(res.text, "html.parser")
    for text in curr_soup.findAll('body'):  
        if re.search("research",text.text.lower()):
            print(a["href"])
            break