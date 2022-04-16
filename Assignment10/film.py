import Media

class Film(Media):
    def __init__(self, type, name ,director ,duration, url, imdb, year, casts):
        Media.__init__(self ,type, name ,director ,duration, url, imdb, year, casts)