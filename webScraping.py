from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from Country import Country
import re



finalistCountries = []
songs = []
places = []
points = []
table = []
Countries = []
years = []

# All the finalists
myUrl = "https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2015"
# Opening connection
eurClient = uReq(myUrl)
pageHtml = eurClient.read()

# html parsing
pageSoup = soup(pageHtml, "html.parser")
# Here is all wikitables where are important results
data = pageSoup.findAll("table",{"class":"wikitable"})
tds = []
firstRow = []
for tab in data:
    # final table data
    if 'Final voting results' in str(tab.caption):
        contentants = tab.find_all("span",{"class":"nobold"})
        results = tab.find_all('tr')


allCountries = []

for contentant in contentants:
    allCountries.append(str(contentant.string))

points = []
pointsFrom = []
tupleList = []
pointsTo = ""
for res in results:
    tds = res.find_all('td')
    for td in tds:
        if td.string == None:
            points.append(0)
        else:
            try:
                point = int(td.string)
                points.append(point)
            except:
                pointsTo = str(td.string.replace("\n",""))
    print("points to " + pointsTo)
    if len(points) < len(allCountries):
        points.append(0)
    print(list(zip(allCountries,points)))
    points.clear()