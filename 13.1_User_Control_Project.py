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
'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

SW = 600
SH = 600
rad = 5
col_list = [0]
color = arcade.color.RED


class Ball:
    def __init__(self, x: int, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c
        self.collisions = 0
        self.explosion = arcade.load_sound("explosion.mp3")
        self.finish = arcade.load_sound("133008__cosmicd__annulet-of-absorption.wav")

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_ball(self):
        global color
        self.x += self.dx
        self.y += self.dy
        self.r += 1 / 120

        if 250 <= self.x <= 350 and self.y - self.r <= 250 <= self.y + self.r:
            self.x = 300
            self.y = 300

            # print("1")

        elif 200 <= self.x <= 400 and self.y - self.r <= 200 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300

        elif 150 <= self.x <= 450 and self.y - self.r <= 150 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300

        elif 100 <= self.x <= 500 and self.y - self.r <= 100 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300

        elif 50 <= self.x <= 550 and self.y - self.r <= 50 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300

        elif 200 <= self.x <= 350 and self.y - self.r <= 350 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 150 <= self.x <= 400 and self.y - self.r <= 400 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 100 <= self.x <= 450 and self.y - self.r <= 450 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 50 <= self.x <= 500 and self.y - self.r <= 500 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 0 <= self.x <= 550 and self.y - self.r <= 550 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 0 <= self.x <= 50 and self.y - self.r <= 500 <= self.y + self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 250 <= self.y <= 350 and self.x + self.r >= 350 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 200 <= self.y <= 400 and self.x + self.r >= 400 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 150 <= self.y <= 450 and self.x + self.r >= 450 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 100 <= self.y <= 500 and self.x + self.r >= 500 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 50 <= self.y <= 550 and self.x + self.r >= 550 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 200 <= self.y <= 350 and self.x + self.r >= 200 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 150 <= self.y <= 400 and self.x + self.r >= 150 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 100 <= self.y <= 450 and self.x + self.r >= 100 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 50 <= self.y <= 500 and self.x + self.r >= 50 >= self.x - self.r:
            arcade.play_sound(self.explosion, 0.5)
            self.x = 300
            self.y = 300
        elif 0 <= self.y <= 575 and self.x + self.r >= 0 >= self.x - self.r:
            arcade.play_sound(self.finish, 0.5)
            color = arcade.color.GREEN


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(True)
        self.ball_list = []
        x_loc = random.randrange(256, 345)
        y_loc = random.randrange(256, 345)
        self.ball = Ball(x_loc, y_loc, 0, 0, rad,
                         (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))
        self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()
        arcade.draw_line(250, 250, 350, 250, color, 1)
        arcade.draw_line(350, 250, 350, 350, color, 1)
        arcade.draw_line(350, 350, 200, 350, color, 1)
        arcade.draw_line(200, 350, 200, 200, color, 1)
        arcade.draw_line(200, 200, 400, 200, color, 1)
        arcade.draw_line(400, 200, 400, 400, color, 1)
        arcade.draw_line(400, 400, 150, 400, color, 1)
        arcade.draw_line(150, 400, 150, 150, color, 1)
        arcade.draw_line(150, 150, 450, 150, color, 1)
        arcade.draw_line(450, 150, 450, 450, color, 1)
        arcade.draw_line(450, 450, 100, 450, color, 1)
        arcade.draw_line(100, 450, 100, 100, color, 1)
        arcade.draw_line(100, 100, 500, 100, color, 1)
        arcade.draw_line(500, 100, 500, 500, color, 1)
        arcade.draw_line(500, 500, 50, 500, color, 1)
        arcade.draw_line(50, 500, 50, 50, color, 1)
        arcade.draw_line(50, 50, 550, 50, color, 1)
        arcade.draw_line(550, 50, 550, 550, color, 1)
        arcade.draw_line(550, 550, 0, 550, color, 1)
        arcade.draw_line(0, 500, 50, 500, color, 1)
        arcade.draw_text("Press Space to Reset", 100, 550, arcade.color.GREEN, 20)

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()

    def on_key_press(self, key: int, modifiers: int):
        global color
        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.ball.dx = 6
        if key == arcade.key.W or key == arcade.key.UP:
            self.ball.dy = 6

        if key == arcade.key.A or key == arcade.key.LEFT:
            self.ball.dx = -6
        if key == arcade.key.S or key == arcade.key.DOWN:
            self.ball.dy = -6

        if key == arcade.key.SPACE:
            self.ball.r = 5
            self.ball.x = 300
            self.ball.y = 300
            color = arcade.color.RED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0

        if key == arcade.key.A or key == arcade.key.D:
            self.ball.dx = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.ball.dy = 0


def main():
    MyGame(SW, SH, "Maze 2")
    arcade.run()


if __name__ == "__main__":
    main()
