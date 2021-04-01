import arcade

SW=600
SH=400

class Ball:
    def __init__(self,x,y,dx,dy,r,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.c=c
        self.laser_sound = arcade.load_sound("explosion.mp3")
    def draw_ball(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)

    def update_ball(self):
        self.x+= self.dx
        self.y+= self.dy


        if self.x < self.r:
            self.dx = 0
            self.x= self.r
            arcade.play_sound(self.laser_sound,5)
        elif self.x > SW - self.r:
            self.dx = 0
            self.x = SW - self.r
            arcade.play_sound(self.laser_sound,5)
        if self.y < self.r:
            self.dy = 0
            self.y = self.r
            arcade.play_sound(self.laser_sound,5)
        elif self.y > SH - self.r:
            self.dy = 0
            self.y = SH - self.r
            arcade.play_sound(self.laser_sound,5)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)
        self.ball = Ball(320,240,0,0,15,arcade.color.ARMY_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.x=x
        self.ball.y=y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse clicked at",x,y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse clicked at",x,y)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx=-4
        elif key ==arcade.key.RIGHT:
            self.ball.dx=4
        elif key == arcade.key.UP:
            self.ball.dy=4
        elif key == arcade.key.DOWN:
            self.ball.dy=-4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0


def main():
    window = MyGame(SW, SH, "Mouse control")
    arcade.run()


if __name__ == "__main__":
    main()