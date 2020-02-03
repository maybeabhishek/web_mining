import requests
from bs4 import BeautifulSoup
import re
import sys


def get_links_recursive(base, path, visited, word,max_depth=3, depth=0):
    if depth < max_depth:
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")

                if href not in visited:
                    visited.add(href)
                    print(f"at depth {depth}: {href}")

                    if href.startswith("http"):
                         if re.search(word,text.text.lower()):
                            print("\n\nFound word ",word," in : ",a["href"],"\n\n")
                            break
                        get_links_recursive(href, "", visited,word, max_depth, depth + 1)
                    else:
                        get_links_recursive(base, href, visited, word,max_depth, depth + 1)
        except:
            pass


num = sys.argv[1]
word = sys.argv[2]
site = sys.argv[3]

get_links_recursive(site, "", set(["http://vit.ac.in"]), word)