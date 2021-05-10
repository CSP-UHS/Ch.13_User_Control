'''
Sign your name: Geni W
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!

'''
import arcade

SW = 500
SH = 500
redSpeed = 3
blueSpeed = 4


class Box:
    def __init__(self, x, y, dx, dy, side, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.c = c
        if self.c == arcade.color.RED:
            self.sound = arcade.load_sound("laser.mp3")
        else:
            self.sound = arcade.load_sound("explosion.mp3")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < self.side/2:
            self.dx = 0
            self.x = self.side/2
            arcade.play_sound(self.sound, 100, -1)
        elif self.x > SW - self.side/2:
            self.dx = 0
            self.x = SW - self.side / 2
            arcade.play_sound(self.sound, 100, 1)
        elif self.y < self.side/2:
            self.dy = 0
            self.y = self.side/2
            arcade.play_sound(self.sound, 100, 0)
        elif self.y > SH - self.side/2:
            self.dy = 0
            self.y = SW - self.side / 2
            arcade.play_sound(self.sound, 100, 0)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ALMOND)
        self.redbox = Box(400, 400, 0, 0, 30, arcade.color.RED)
        self.bluebox = Box(100, 100, 0, 0, 30, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.redbox.draw_box()
        self.bluebox.draw_box()

    def on_update(self, dt):
        self.redbox.update_box()
        self.bluebox.update_box()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bluebox.dx = -blueSpeed
        elif key == arcade.key.RIGHT:
            self.bluebox.dx = blueSpeed
        elif key == arcade.key.UP:
            self.bluebox.dy = blueSpeed
        elif key == arcade.key.DOWN:
            self.bluebox.dy = -blueSpeed
        elif key == arcade.key.A:
            self.redbox.dx = -redSpeed
        elif key == arcade.key.D:
            self.redbox.dx = redSpeed
        elif key == arcade.key.W:
            self.redbox.dy = redSpeed
        elif key == arcade.key.S:
            self.redbox.dy = -redSpeed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bluebox.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.bluebox.dy = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.redbox.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.redbox.dy = 0


def main():
    window = MyGame(SW, SH, "Jedi Training 13")
    arcade.run()


if __name__ == "__main__":
    main()