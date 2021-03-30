'''
Sign your name:Daniel
 
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
import random

SW = 500
SH = 500



class Box():
    def __init__(self, x, y, speed, r, c, CS):
        self.x = x
        self.y = y
        self.speed = speed
        self.r = r
        self.color = c
        self.CS = CS
        self.dx = 0
        self.dy = 0
        self.wallhit = arcade.load_sound("laser.mp3")

    def control(self,key):
        #print(key)
        if self.CS == "wasd":
            if key == 119:
                self.dy = self.speed
            if key == 97:
                self.dx = -self.speed
            if key == 115:
                self.dy = -self.speed
            if key == 100:
                self.dx = self.speed

        if self.CS == "arrows":
            if key == 65362:
                self.dy = self.speed
            if key == 65361:
                self.dx = -self.speed
            if key == 65364:
                self.dy = -self.speed
            if key == 65363:
                self.dx = self.speed

    def stop(self,key):
        #print(key)
        if self.CS == "wasd":
            if key == 119:
                self.dy = 0
            if key == 97:
                self.dx = 0
            if key == 115:
                self.dy = 0
            if key == 100:
                self.dx = 0

        if self.CS == "arrows":
            if key == 65362:
                self.dy = 0
            if key == 65361:
                self.dx = 0
            if key == 65364:
                self.dy = 0
            if key == 65363:
                self.dx = 0


    def drawbox(self):
        arcade.draw_rectangle_filled(self.x,self.y,2*self.r,2*self.r,self.color)

    def updatebox(self):

        self.x += self.dx
        self.y += self.dy

        if self.x > (500 - self.r):
            self.x = 500 - self.r
            self.dx = 0
            arcade.play_sound(self.wallhit,1)
        if self.y > (500 - self.r):
            self.y = 500 - self.r
            self.dy = 0
            arcade.play_sound(self.wallhit, 1)
        if self.y < (0 + self.r):
            self.y = 0 + self.r
            self.dy = 0
            arcade.play_sound(self.wallhit, 1)
        if self.x < (0 + self.r):
            self.x = 0 + self.r
            self.dx = 0
            arcade.play_sound(self.wallhit, 1)



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)


        self.box_list = []
        box1 = Box(200,250,24,30,arcade.color.BLUE,"arrows")
        self.box_list.append(box1)
        box2 = Box(300,250,18,30,arcade.color.RED,"wasd")
        self.box_list.append(box2)



    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.drawbox()

    def on_update(self, dt):
        for box in self.box_list:
            box.updatebox()

    def on_key_press(self, symbol, modifiers: int):
        for box in self.box_list:
            box.control(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        print(symbol)
        for box in self.box_list:
            box.stop(symbol)





def main():
    mywindow = MyGame(SW, SH, "Jedi Training")
    arcade.run()


if __name__ == "__main__":
    main()