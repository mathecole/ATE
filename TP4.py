import arcade
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

COLORS = []


class Balle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.rayon = random.randint(6, 15)
        self.color = random.choice(COLORS)
    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, color=self.color)
    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT -self.rayon:
            self.change_y *= -1


class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = random.randint(4,6)
        self.height = random.randint(6,12)
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.color = random.choice(COLORS)
        self.angle = random.uniform(0,90)

    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.height:
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
        for i in self.liste_rectangles:
            i.on_draw()

    def on_update(self, delta_time: float):
        for i in self.liste_balles:
            i.on_update()
        for i in self.liste_rectangles:
            i. on_update()

    def on_mouse_press(self, x, y, modifiers, button):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle_child = Balle(x, y)
            self.liste_balles.append(balle_child)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle_child = Rectangle(x, y)
            self.liste_rectangles.append(rectangle_child)


def main():
    my_game = MyGame()
    arcade.run()


main()
