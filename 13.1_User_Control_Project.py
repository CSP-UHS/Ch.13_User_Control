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

'''
import arcade
import random

sw = 500
sh = 500
speed = 4
speed1 = 3
FN = 20


class Box:
    def __init__(self, x, y, dx, dy, side, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.c = c
        #self.cat = arcade.load_sound("")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy
        self.y += self.dy

        if self.x < self.side/2:
            self.dx = 0
            self.x = self.side/2
           # arcade.play_sound(self.cat)
        elif self.x > sw - self.side/2:
            self.dx = 0
            self.x = sw - self.side/2
           # arcade.play_sound(self.cat)
        if self.y < self.side/2:
            self.dy = 0
            self.y = self.side/2
           # arcade.play_sound(self.cat)
        elif self.y > sh - self.side/2:
            self.y = 0
            self.y = sh - self.side/2
           # arcade.play_sound(self.cat)


class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        self.boxlist = []
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ALMOND)
        for i in range(FN):
            side = 100
            dy = -3
            x = random.randint(0, sw)
            y = random.randint(0, sh)
            c = arcade.color.RED
            make_box = Box( x, y,side,side, dy, c)
            self.boxlist.append(make_box)
        self.box = Box(400, 400, 0, 0, 30, arcade.color.BLUE)
        self.box1 = Box(100, 100, 0, 0, 30, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        for box in self.boxlist:
            box.draw_box()
        self.box.draw_box()
        self.box1.draw_box()


    def on_update(self, dt):
        for box in self.boxlist:
            box.update_box()
        self.box.update_box()
        self.box1.update_box()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.box.dx = -speed
        elif key == arcade.key.RIGHT:
            self.box.dx = speed
        elif key == arcade.key.UP:
            self.box.dy = speed
        elif key == arcade.key.DOWN:
            self.box.dy = -speed

        if key == arcade.key.A:
            self.box1.dx = -speed1
        elif key == arcade.key.D:
            self.box1.dx = speed1
        elif key == arcade.key.W:
            self.box1.dy = speed1
        elif key == arcade.key.S:
            self.box1.dy = -speed1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.box.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.box1.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.box1.dy = 0


def main():
    my_window = MyGame(sw, sh, "mouse control")

    arcade.run()


if __name__ == "__main__":
    main()
