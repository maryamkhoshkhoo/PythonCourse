from media import Media

class Documentory(Media):
    def __init__(self, type, name ,director ,duration, url, imdb, year, casts, p):
        Media.__init__(self ,type, name ,director ,duration, url, imdb, year, casts)
        self.parts = p