import arcade
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        x = 400
        y = 300

        arcade.draw_circle_filled(400, 300, 30, (255, 54, 34))
    def on_update(self):
        xchange =10
        pass


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
