class movie:
    def __init__(self,movie,artist,year,ratings):
        self.movie=movie
        self.artist=artist
        self.year=year
        self.ratings=ratings
    def display(self):
        print("name of movie: %s" %self.movie)
        print("name of artist: %s" % self.artist)
        print("year of release: %d" % self.year)
        print("ratings of movie: %s" % self.ratings)


    def update(self):
        self.movie= str(input("enter the name of the movie "))
        self.artist = str(input("enter the name of the artist"))
        self.year = int(input("enter the year of release"))
        self.ratings = str(input("enter the ratings for movie"))

a= str(input("enter the name of the movie"))
b = str(input("enter the name of the artist"))
c = int(input("enter the year of release"))
d= str(input("enter the ratings for movie"))
z=movie(a,b,c,d)
z.display()
n=int(input("do you want to change the movie details"))
if(n==0):
    z.update()
    z.display()
else:
    z.display()
