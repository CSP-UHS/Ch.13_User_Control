'''
Sign your name:_______RYan MueYzet_________
 
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

screen_width = 500
screen_height = 500


class Box:
    def __init__(self, x, y, dx, dy, side, color, speed):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.color = color
        self.speed = speed

        if self.color == arcade.color.RED:
            self.wall_sound = arcade.load_sound("explosion.mp3")
        else:
            self.wall_sound = arcade.load_sound("laser.mp3")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.color)

    def box_update(self):
        self.x += self.dx
        self.y += self.dy


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.box_red = Box(100, 100, 0, 0, 30, arcade.color.RED, 3)
        self.box_blue = Box(400, 400, 0, 0, 30, arcade.color.BLUE, 4)

    def on_draw(self):
        arcade.start_render()
        self.box_red.draw_box()
        self.box_blue.draw_box()

    def on_update(self, delta_time: float):
        self.box_red.box_update()
        self.box_blue.box_update()

        if self.box_red.x + (self.box_red.side/2) >= screen_width:  # if the edge of the red box hits the edge
            self.box_red.x = 485                                    # then stop it to stay at the edge
            arcade.play_sound(self.box_red.wall_sound)              # and then play a sound
        elif self.box_red.x - (self.box_red.side/2) <= 0:
            self.box_red.x = 15
            arcade.play_sound(self.box_red.wall_sound)
        if self.box_red.y + (self.box_red.side/2) >= screen_height:
            self.box_red.y = 485
            arcade.play_sound(self.box_red.wall_sound)
        elif self.box_red.y - (self.box_red.side / 2) <= 0:
            self.box_red.y = 15
            arcade.play_sound(self.box_red.wall_sound)

        if self.box_blue.x + (self.box_blue.side / 2) >= screen_width:  # if the edge of the red box hits the edge
            self.box_blue.x = 485  # then stop it to stay at the edge
            arcade.play_sound(self.box_blue.wall_sound)
        elif self.box_blue.x - (self.box_blue.side / 2) <= 0:
            self.box_blue.x = 15
            arcade.play_sound(self.box_blue.wall_sound)
        if self.box_blue.y + (self.box_blue.side / 2) >= screen_height:
            self.box_blue.y = 485
            arcade.play_sound(self.box_blue.wall_sound)
        elif self.box_blue.y - (self.box_blue.side / 2) <= 0:
            self.box_blue.y = 15
            arcade.play_sound(self.box_blue.wall_sound)

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.W:         # if a specific key is pressed then move the red ball in the direction
            self.box_red.dy = self.box_red.speed
        elif key == arcade.key.S:
            self.box_red.dy = -self.box_red.speed
        if key == arcade.key.D:
            self.box_red.dx = self.box_red.speed
        elif key == arcade.key.A:
            self.box_red.dx = -self.box_red.speed

        if key == arcade.key.LEFT:      # if a specific key is pressed then move the red ball in the direction
            self.box_blue.dx = -self.box_blue.speed
        elif key == arcade.key.RIGHT:
            self.box_blue.dx = self.box_blue.speed
        if key == arcade.key.UP:
            self.box_blue.dy = self.box_blue.speed
        elif key == arcade.key.DOWN:
            self.box_blue.dy = -self.box_blue.speed

    def on_key_release(self, key, modifiers: int):  # if a key is released then stop movement in that direction
        if key == arcade.key.W or key == arcade.key.S:
            self.box_red.dy = 0                     # red box
        if key == arcade.key.A or key == arcade.key.D:
            self.box_red.dx = 0

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.box_blue.dy = 0                    # blue box
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box_blue.dx = 0


def main():
    window = Render(screen_width, screen_height, "Box Example")
    arcade.run()


if __name__ == "__main__":
    main()

'''
# example ball code
# it will just print a ball on the cursor position

import arcade


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball = Ball(50, 50, 15, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.ball.x = x
        self.ball.y = y


def main():
    window = Render(500, 500, "Ball Example")
    arcade.run()


if __name__ == "__main__":
    main()
'''
