from media import Media

class Series(Media):
    def __init__(self, type, name ,director ,duration, url, imdb, year, casts, p):
        Media.__init__(self ,type, name ,director ,duration, url, imdb, year, casts)
        self.parts = p

    def show_info(self):
        Media.show_info(self)
        print(self.parts)