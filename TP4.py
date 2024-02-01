import arcade
import random
import time

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

COLORS = []


class Balle(self, x, y):
    def __init__(self):
        self.x = x
        self.y = y
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.rayon = random.randint(6, 15)
        self.color = random.choice(Colours)
    def on_draw(self):
        arcade.draw_criclefilled(self.x, self.y, self.rayon, color = self.color)
    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT -self.rayon:
            self.change_y *= -1


class Rectangle(self, x, y):
    def __init__(self):
        self.x = x
        self.y = y
        self.width = random.randint(4,6)
        self.height = random.randint(6,12)
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.color = random.choice(Colours)
        self.angle = random.uniform(0,90)

    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1
        if self.Y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1


    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, color = self.color, tilt_angle=self.angle)
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_balles = []
        self.liste_rectangles = []


    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        for i in self.liste_balles:
            i.on_draw()
        for i in self.liste_rectangles
            i.on_draw()

    def on_update(self, float, delta_time):
        pass

    def on_mouse_press(self, x, y, modifiers, button):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle_child = Balle(x, y)
            self.liste_balles.append(balle_child)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle_child = Rectangle(x, y)
            self.liste_rectangles.append(rectangle_child)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
