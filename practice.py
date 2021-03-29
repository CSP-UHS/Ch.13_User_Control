import arcade

SW=640
SH=480

class Ball:
    def __init__(self,x,y,dx,dy,r,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.c=c

    def draw_ball(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)

    # def update_ball(self):
    #     self.x+= self.dx
    #     self.y+= self.dy


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)
        self.ball = Ball(320,240,3,-2,15,arcade.color.ARMY_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    # def on_update(self, dt):
    #     self.ball.update_ball()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.x=x
        self.ball.y=y


def main():
    window = MyGame(SW, SH, "Mouse control")
    arcade.run()


if __name__ == "__main__":
    main()