from bs4 import BeautifulSoup
import requests
import re
import unittest


# search = input("Search For:")
# params = {"q": search}

# Get monster entries from d20 srd
r = requests.get("http://www.d20srd.org/indexes/monsters.htm")

soup = BeautifulSoup(r.text, "html.parser")

# search soup for monster page hyperlinks
for result in soup.find_all(href=re.compile("monsters")):
    # print("{}: {}".format(result.string, result.attrs))
    url = str("http://www.d20srd.org" + result.attrs["href"])
    # print('{}'.format(url))
    # get stat tables for each monster entry
    entry = requests.get(url=url)
    entry_soup = BeautifulSoup(entry.text, "html.parser")

# TODO
