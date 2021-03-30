'''
Sign your name:Jacob Walters
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the ASDW keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!

'''
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

    def update_ball(self):
        self.x+= self.dx
        self.y+= self.dy

        if self.x <= self.r or self.x >= SW - self.r:
            self.dx *= -1
        if self.y <= self.r or self.y >= SH - self.r:
            self.dy *= -1



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.ball = Ball(320,240,3,-2,15,arcade.color.ARMY_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()

def main():
    window = MyGame(SW, SH, "Window")
    arcade.run()


if __name__ == "__main__":
    main()