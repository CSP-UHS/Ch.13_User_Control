import arcade

SW = 640
SH = 480


class Ball:
    def __init__(self, x, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < self.r or self.x >= SW - self.r:
            self.dx *= -1
        if self.y < self.r or self.y >= SH - self.r:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ALMOND)
        self.ball = Ball(320.5, 240, 0, 0, 15, arcade.color.BLUE_SAPPHIRE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()


# def on_mouse_motion(self, x, y, dx, dy):
#    self.ball.x = x
#   self.ball.y = y

# def on_mouse_press(self, x, y, button, modifiers):
#    if button == arcade.MOUSE_BUTTON_LEFT:
#       print("Left mouse button clicked at", x, y)
#  elif button == arcade.MOUSE_BUTTON_RIGHT:
#     print("Right mouse button clicked at", x, y)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -4
        elif key == arcade.key.RIGHT:
            self.ball.dx = 4
        elif key == arcade.key.UP:
            self.ball.dy = 4
        elif key == arcade.key.DOWN:
            self.ball.dy = -4


def main():
    window = MyGame(SW, SH, "Mouse Control Example")
    arcade.run()


if __name__ == "__main__":
    main()
