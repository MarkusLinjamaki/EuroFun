from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from Country import Country

myUrl = "https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2018"
# Opening connection
eurClient = uReq(myUrl)
pageHtml = eurClient.read()


# html parsing
pageSoup = soup(pageHtml, "html.parser")


data = pageSoup.findAll("table",{"class":"sortable wikitable plainrowheaders"})


finalistCountries = []
singers = []
songs = []
places = []
points = []

for ind in range(len(data)):
    if not not data[ind].findAll("tr",{"style":"font-weight:bold; background:gold;"}):
        table = data[ind].findAll("td")
        break

ind = 0
laskuri = 0
for td in table:
    inf = td.a
    if inf != None:  
        try:
            inf = str(inf['title'])
            if ind % 3 == 0 and "Eurovision" in inf:
                finalistCountries.append(inf.split()[0])
            if ind % 3 == 1:
                singers.append(inf)
            if ind % 3 == 2:
                songs.append(inf)
        except:
            pass
    else:
        point = str(td)
        point = point.replace("</td>","")
        point = point.replace("<td>","")
        point = point.replace("\n","")
        try:
            point = int(point)
            if laskuri % 2 == 1:
                points.append(point)
            if laskuri % 2 == 0:
                places.append(point)

        except:
            pass
    laskuri = laskuri + 1
    ind = ind + 1

#print(*finalistCountries)
#print(*singers)
#print(*songs)
#print(*points)
#print(*places)

#Close connection
eurClient.close()

if(len(finalistCountries) != len(singers) != len(songs)):
    print("Joko maat, laulajat tai biisit liikaa..")

Countries = []
for a in range(len(finalistCountries)):
    Countries.append(Country(finalistCountries[a], singers[a], songs[a], places[a], points[a]))

for a in Countries:
    print(a.name + " " + a.singer + " " + a.song + " " + str(a.place) + " " + str(a.points))

