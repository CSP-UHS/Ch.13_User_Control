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

SW=500
SH=500

class Box:
    def __init__(self,x,y,dx,dy,w,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.w=w
        self.c=c
        self.laser_sound = arcade.load_sound("laser.mp3")
    def draw_box(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.w,self.w,self.c)

    def update_box(self):
        self.x+= self.dx
        self.y+= self.dy


        if self.x < self.w:
            self.dx = 0
            self.x= self.w
            arcade.play_sound(self.laser_sound,5)
        elif self.x > SW - self.w:
            self.dx = 0
            self.x = SW - self.w
            arcade.play_sound(self.laser_sound,5)
        if self.y < self.w:
            self.dy = 0
            self.y = self.w
            arcade.play_sound(self.laser_sound,5)
        elif self.y > SH - self.w:
            self.dy = 0
            self.y = SH - self.w
            arcade.play_sound(self.laser_sound,5)

class Box_2:
    def __init__(self,x,y,dx,dy,w,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.w=w
        self.c=c
        self.explosion_sound = arcade.load_sound("explosion.mp3")
    def draw_box2(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.w,self.w,self.c)

    def update_box2(self):
        self.x+= self.dx
        self.y+= self.dy


        if self.x < self.w:
            self.dx = 0
            self.x= self.w
            arcade.play_sound(self.explosion_sound,5)
        elif self.x > SW - self.w:
            self.dx = 0
            self.x = SW - self.w
            arcade.play_sound(self.explosion_sound,5)
        if self.y < self.w:
            self.dy = 0
            self.y = self.w
            arcade.play_sound(self.explosion_sound,5)
        elif self.y > SH - self.w:
            self.dy = 0
            self.y = SH - self.w
            arcade.play_sound(self.explosion_sound,5)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)
        self.box = Box(320,240,0,0,30,arcade.color.BLUE)
        self.box2 = Box_2(320,240,0,0,30,arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.box.draw_box()

    def on_update(self, dt):
        self.box.update_box()

    def on_draw2(self):
        arcade.start_render()
        self.box2.draw_box2()

    def on_update2(self, dt):
        self.box2.update_box2()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.box.dx=-4
        elif key ==arcade.key.RIGHT:
            self.box.dx=4
        elif key == arcade.key.UP:
            self.box.dy=4
        elif key == arcade.key.DOWN:
            self.box.dy=-4
        if key == arcade.key.A:
            self.box2.dx=-3
        elif key == arcade.key.D:
            self.box.dx=3
        elif key == arcade.key.W:
            self.box.dy=3
        elif key == arcade.key.S:
            self.box.dy=-3

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.box.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.box.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.box.dy = 0
            a
def main():
    window = MyGame(SW, SH, "Mouse control")
    arcade.run()


if __name__ == "__main__":
    main()