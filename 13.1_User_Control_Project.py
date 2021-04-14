'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.

haha get the cs
click the minion when its health is low
if you do it good then you get money

'''

import arcade


class Crosshair:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw_crosshair(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size / 5, self.color)
        arcade.draw_rectangle_filled(self.x, self.y, self.size / 5, self.size, self.color)


class Minion:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)

        self.crosshair = Crosshair(100, 100, 20, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.crosshair.draw_crosshair()

    def on_update(self, delta_time: float):
        placeholder = 0

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.crosshair.x = x
        self.crosshair.y = y


def main():
    window = Render(800, 600, 'CS')
    arcade.run()


if __name__ == '__main__':
    main()
