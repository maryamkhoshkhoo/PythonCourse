from ast import fix_missing_locations
from numpy import append
from clip import Clip
from documentary import Documentary 
from film import Film
from series import Series
from media import Media
from actor import Actor

class Main:

    def __init__(self):
        file = open('database.txt','r')
        line = file.read().split('\n')
        self.movie = []

        for i in range(len(line)):
            info = line[i].split(',')
            if info[0] == 'film':
                self.movie.append(Film(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))

            elif info[0] == 'series':
                self.movie.append(Series(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8]))
            
            elif info[0] == 'clip':
                self.movie.append(Clip(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7])) 

            elif info[0] == 'documentary':
                self.movie.append(Documentary(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8]))
                
                 
        file.close()
        Main.menu(self)

    def menu(self):

        while True:
            print('0.Show list')
            print('1.Add')
            print('2.Edit')
            print('3.Delet')
            print('4.Search')
            print('5.Advance search')
            print('6.Download')
            print('7.Exit')
            x = int(input('Please enter the number: '))

            if x == 0:
                Main.show_list(self)
            
            if x == 1:
                Main.add(self)

            elif x == 2:
                Main.edit(self)
    
            elif x == 3:
                Main.delete(self)

            elif x == 4:
                Main.search(self)
    
            elif x == 5:
                Main.search_advance(self)

            elif x == 6:
                Main.download(self)

            elif x == 7:                  
                Main.save(self)
                break
    
    def show_list(self):

        for i in self.movie :

            if i.type == 'series' or i.type == 'documentary':
                Series.show_info(i)
                
            else:
                Media.show_info(i)
                

    def add(self):
        new_type = input('Write type of the media: \nfilm\nserial\nclip\ndocumentry: ')
        new_name = input('Enter name: ')
        new_director = input('Enter director: ')
        new_imdb = input('Enter imdb score: ')
        new_url = input('Enter url: ')
        new_duration = input('Enter duration(minute): ')
        new_year = input('Enter year: ')
        new_casts = input('Enter casts: ')

        if new_type == 'film':
            self.movie.append(Film(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts))

        elif new_type == 'clip':
            self.movie.append(Clip(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts))

        elif new_type == 'series':
            new_part = input('Enter number of episods: ')
            self.movie.append(Series(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts, new_part)) 

        elif new_type == 'documentary' :
            new_part = input('Enter number of episods: ')
            self.movie.append(Documentary(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts, new_part))
        
        print('add done!')
    
    def edit(self):
        k = 0
        m = input('Enter name of the movie: ')

        for movie in self.movie:
            if m == movie.name:
                k = 1
                if movie.type == 'series' :
                    Series.edit_series(movie)
                elif movie.type == 'documentary':
                    Documentary.edit_doc(movie)
                elif movie.type == 'film':
                    Film.edit_film(movie)
                elif movie.type == 'clip':
                    Clip.edit_clip(movie)                   
                print('Edit done') 
                
        if k == 0:
            print('not fonded')

    def delete(self):
        n = input('Enter name of the movie: ')

        for movie in self.movie :
            if n == movie.name :
                self.movie.remove(movie)
                print('Delete done!')
                break

            if movie == len(self.movie) and n!= movie.name:
                print('not found')

    def search(self):
        k = 1
        n = input('Enter name of the movie:')
        for i in self.movie :
            if n == i.name :
                Media.show_info(i)
                k = 0
        if k == 1:
            print('not found')        

    def search_advance(self):
        k = 0
        a = int(input('Enter first time: '))
        b = int(input('Enter second time: '))

        for i in self.movie:
            if a <= int(i.duration) <= b :
                Media.show_info(i)
                k = 1
        if k == 0 :
            print('not exist')        
    
    def download(self):
        n = input('Enter name of the movie: ')

        for movie in self.movie:
            if n == movie.name :
                Media.download(movie)
              

    def save(self):
        file = open('database.txt','w')

        for i in self.movie:
            if i.type == 'series' or i.type == 'documentary' : 
                if i != len(self.movie)-1 :
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts +','+ i.parts + '\n'
                else:
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts +','+ i.parts            
                file.write(str1)

            elif i.type == 'film' or i.type == 'clip' :
                if i != len(self.movie)-1 :
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts +'\n'
                else:
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts
                file.write(str1)
            
        file.close()

Main()  