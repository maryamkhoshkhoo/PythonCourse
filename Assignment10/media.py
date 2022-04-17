from numpy import append
import pytube

class Media:
    def __init__(self ,type, name ,director ,duration, url, imdb, year, casts):
        self.type = type
        self.name = name
        self.director = director
        self.duration = duration 
        self.url = url
        self.IMDBscore = imdb
        self.year = year
        self.casts = casts

    def show_info(self):  
        print(self.type+'\n'+self.name+'\n'+self.director+'\n'+ self.duration +'\n'+self.url+'\n'+ self.IMDBscore + '\n'+self.year+ '\n'+self.casts)
    
    def download(self):
        link = self.url
        first_stream =pytube.YouTube(link).streams.first()
        first_stream.download(output_path = './' , filename = 'dl.mp4')
        print('Download is complete!')