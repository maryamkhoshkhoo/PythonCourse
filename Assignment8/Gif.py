import imageio
import os

images = []
for file_name in os.listdir('images'):
    image = imageio.imread(f'images/{file_name}')
    images.append(image) #poshtesarham namayesh mide axaro
    
imageio.mimsave('baby.gif', images)  