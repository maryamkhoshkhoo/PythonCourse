from media import Media

class Documentary(Media):
    def __init__(self, type, name ,director ,duration, url, imdb, year, casts, p):
        Media.__init__(self ,type, name ,director ,duration, url, imdb, year, casts)
        self.parts = p 

    def edit_doc(self):
        j = int(input('1-edit name\n2-edit director\n3-edit imdb\n4-url\n5-edit duration\n6-edit year\n7-edit casts: '))
        if j==1 :
            self.name = input('Enter name: ')    
        
        elif j==2:
            self.director = input('Enter director: ') 

        elif j==3:
            self.IMDBscore = input('Enter imdb: ')
        
        elif j==4:
            self.url = input('Enter url: ')

        elif j==5:
            self.duration = input('Enter duration (minute): ')
        
        elif j==6:
            self.year = input('Enter year: ')
        
        elif j==7: 
            self.casts = input('Enter casts: cast1-cast2... ')
        
        elif j==8:
            self.parts = input('Enter namber of parts: ')  