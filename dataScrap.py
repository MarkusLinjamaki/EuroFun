from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from Country import Country



finalistCountries = []
songs = []
places = []
points = []
table = []
Countries = []
years = []

# All the finalists
for a in range(1990,2018):
    myUrl = "https://en.wikipedia.org/wiki/Eurovision_Song_Contest_" + str(a)
    # Opening connection
    eurClient = uReq(myUrl)
    pageHtml = eurClient.read()

    # html parsing
    pageSoup = soup(pageHtml, "html.parser")

    # Finalist data from table
    data = pageSoup.findAll("table",{"class":"sortable wikitable plainrowheaders"})
    # Finalist table includes one cell with golden marginal
    for ind in range(len(data)):
        if not not data[ind].findAll("tr",{"style":"font-weight:bold; background:gold;"}):
            table = data[ind].findAll("td")
            break

    ind = 0
    calc = 0
    for td in table:
        inf = td.a
        if inf != None:  
            try:
                inf = str(inf['title'])
                if ind % 3 == 0 and "Eurovision" in inf:
                    finalistCountries.append(inf.split()[0])
                if ind % 3 == 2:
                    songs.append(inf)
            except:
                pass
        else:
            point = str(td)
            # Stripping
            point = point.replace("</td>","")
            point = point.replace("<td>","")
            point = point.replace("\n","")
            point = point.replace("\"","")

            # Norge 2009
            point = point.replace("<span data-sort-value=01","")
            point = point.replace("!>","")
            point = point.replace("</span>","")

            try:
                point = int(point)
                if calc % 2 == 1:
                    points.append(point)
                if calc % 2 == 0:
                    places.append(point)
            except:
                pass
        calc = calc + 1
        ind = ind + 1
    if(len(finalistCountries) == len(songs) == len(places) == len(points)):
        print("Year " + str(a) + " downloaded")
    
    finalistCountries.clear()
    songs.clear()
    places.clear()
    points.clear()

#for a in range(len(finalistCountries)):
#    Countries.append(Country(finalistCountries[a], singers[a], songs[a], places[a], points[a]))

#Close connection
eurClient.close()

#for a in Countries:
#   print(a.name + " " + a.singer + " " + a.song + " " + str(a.place) + " " + str(a.points))


