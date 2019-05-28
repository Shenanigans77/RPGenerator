from bs4 import BeautifulSoup
from lxml import html
import requests
import re
import unittest
import json


# search = input("Search For:")
# params = {"q": search}

# Get monster entries from d20 srd
r = requests.get("http://www.d20srd.org/indexes/monsters.htm")

soup = BeautifulSoup(r.text, "lxml")

# search soup for monster page hyperlinks
for result in soup.find_all(href=re.compile("monsters")):
    print("{}: {}".format(result.string, result.attrs))
    url = str("http://www.d20srd.org" + result.attrs["href"])
    print('{}'.format(url))
    # get stat tables for each monster entry
    entry = requests.get(url=url)
    
    #print("{}".format(entry))
    entry_soup = BeautifulSoup(entry.text, "lxml")
    
    print("{}".format(entry_soup))

# TODO
# http://www.d20srd.org/indexes/monsters.htm
# http://www.d20srd.org/srd/monsters/aboleth.htm
# http://www.d20srd.org/srd/monsters/etherealFilcher.htm