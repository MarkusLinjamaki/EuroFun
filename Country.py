class Country:
    def __init__(self,name,singer,song,place,points):
        self.name = name
        self.singer = singer
        self.song = song
        self.place = place
        self.points = points

    def __str__(self):
        return self.name
    


