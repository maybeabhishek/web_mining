import requests
from bs4 import BeautifulSoup
from collections import deque

visited = set(["http://vit.ac.in"])
dq = deque([["http://vit.ac.in", "", 0]])
max_depth = 3
import re
import sys

word = sys.argv[1]
site = sys.argv[2]

while dq:
    base, path, depth = dq.popleft()
    

    if depth < max_depth:
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")

                if href not in visited:
                    visited.add(href)
                     if re.search(word,text.text.lower()):
                        print("\n\nFound word ",word," in : ",a["href"],"\n\n")
                        break
                    # print("  " * depth + f"at depth {depth}: {href}")

                    if href.startswith("http"):
                        dq.append([href, "", depth + 1])
                    else:
                        dq.append([base, href, depth + 1])
        except:
            pass