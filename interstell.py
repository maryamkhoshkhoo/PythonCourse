import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Spaceship:
    pass


class Enemy:
    pass


class Bullet:
    pass


class Game(arcade.Window):
    def __init__(self):
        super().__init__(600, 800, "interstell")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_1rwh_rectangle_texture(100, 50, 300, 400, self.background_image)

game = Game()
arcade.run() 
