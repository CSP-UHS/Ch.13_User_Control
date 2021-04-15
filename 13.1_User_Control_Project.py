

import arcade
import random

SW = 500
SH = 500
coinnum = 0

class Player():
    def __init__(self, x, y, speed, r, c, CS,grav):
        self.x = x
        self.y = y
        self.speed = speed
        self.r = r
        self.color = c
        self.CS = CS
        self.dx = 0
        self.dy = 0
        self.tilt = 0
        self.grav = grav
        self.woosh = arcade.load_sound("woosh.flac")
        if c == arcade.color.BLUE:
            self.wallhit = arcade.load_sound("laser.mp3")
        else:
            self.wallhit = arcade.load_sound("explosion.mp3")

    def control(self, key):
        global coinnum
        if key == 32:
            self.dy = self.dy + 5 + (coinnum * 0.3)
            arcade.play_sound(self.woosh,0.8)
        if key == 99:
            coinnum +=1

        # print(key)


    def drawplayer(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.r, self.r, self.color,self.tilt)
        arcade.draw_text(str(coinnum),50,50,arcade.color.BLACK,20)

    def updateplayer(self):

        self.x += self.dx
        self.y += self.dy
        self.dy += ((self.grav/60) - (coinnum * 0.03))

        self.tilt = -3 * self.dy


        if self.y > (500 - self.r * 0.5):
            self.y = 500 - self.r * 0.5
            self.dy = -self.dy
            arcade.play_sound(self.wallhit, 1)
        if self.y < (0 + self.r * 0.5):
            self.y = 0 + self.r * 0.5
            self.dy = -self.dy
            arcade.play_sound(self.wallhit, 1)


class World():
    def __init__(self, speed,x,y,c):
        self.speed = speed
        self.x = x
        self.y = y
        self.orgiinx = x
        self.coin = c
        self.wallhit = arcade.load_sound("explosion.mp3")
        self.coinsound = arcade.load_sound("coin.wav")



    def drawworld(self):
        #arcade.draw_rectangle_filled(self.x,self.y,20,40,arcade.color.RED)
        arcade.draw_lrtb_rectangle_filled(self.x - 10, self.x + 10,self.y,0,arcade.color.RED)
        arcade.draw_lrtb_rectangle_filled(self.x - 10, self.x + 10, 590, self.y + 280, arcade.color.RED)
        #arcade.draw_text(str(self.coinnum),50,50,arcade.color.BLACK,20)

        if self.coin == "coin":
            arcade.draw_circle_filled(self.x,self.y + 50,15,arcade.color.GOLD)
            arcade.draw_circle_filled(self.x, self.y + 50, 10, arcade.color.DARK_GOLDENROD)


    def updateworld(self):
        if self.speed != 0:
            self.x += (self.speed - (coinnum * 0.2))

    def explode(self):
        arcade.play_sound(self.wallhit)

    def coincol(self):
        global coinnum
        if self.coin == "coin":
            arcade.play_sound(self.coinsound)
            coinnum += 1
            self.coin = "nocoin"

    def loss(self):
        self.speed = 0
        print("loss")
        self.x = self.x +1

    def reset(self):
        #global coinnum
        self.x = self.orgiinx
        self.speed = -1
        #coinnum = 0


class Backround():
    def __init__(self, speed,x,y,h):
        self.speed = speed
        self.x = x
        self.y = y
        self.h = h

    def drawmount(self):
        if self.x > -200 and self.x < 700:
            arcade.draw_rectangle_filled(self.x,self.y,self.h,self.h,arcade.color.GREEN,45)
            arcade.draw_rectangle_outline(self.x, self.y, self.h, self.h, arcade.color.GRAY,1,45)

    def updatemont(self):
        self.x += self.speed
        if self.x < -200:
            self.x = random.randint(700,900)

class Text():
    def __init__(self, speed):
        self.speed = speed
        self.x = 200
        self.y = 200

    def draw(self):
        arcade.draw_text("Space: Flap \n R: Restart",self.x,self.y,arcade.color.BLACK )

    def update(self):
        self.x += self.speed





class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player1 = Player(200, 250, 4, 30, arcade.color.BLUE, "arrows",-3.5)

        self.intructions = Text(-1)

        self.backlist = []
        for i in range(25):
            background = Backround(-0.5,random.randint(-200,700),0,random.randint(50,200))
            self.backlist.append(background)

        self.worldlist = []
        x = 300
        for i in range(100):
            x += 100
            if random.randint(0,4) == 0:
                pillar = World(-1, x, random.randint(10, 300), "coin")
            else:
                pillar = World(-1,x,random.randint(10,300),"nocoin")
            self.worldlist.append(pillar)



    def on_draw(self):
        arcade.start_render()


        for obj in self.backlist:
            obj.drawmount()

        self.player1.drawplayer()

        for obj in self.worldlist:
            if obj.x < 520 and obj.x > -20:
                obj.drawworld()

        self.intructions.draw()


    def on_update(self, dt):

        for obj in self.backlist:
            obj.updatemont()

        self.player1.updateplayer()

        for obj in self.worldlist:
            obj.updateworld()
            if obj.x >= 100 and obj.x <= 400:
                if self.player1.y - (self.player1.r * 0.5) < obj.y and abs(self.player1.x + (0.5 *self.player1.r) - obj.x) <= 10:
                    #print("loss")
                    obj.explode()
                    for pillar in self.worldlist:
                        pillar.loss()

                if self.player1.y + (self.player1.r *0.5) > obj.y + 280 and abs(self.player1.x + (0.5* self.player1.r) - obj.x) <= 10:
                    #print("loss")
                    obj.explode()
                    for obj in self.worldlist:
                        obj.loss()

                if self.player1.y - self.player1.r < obj.y + 50 and abs(self.player1.x + (0.5 *self.player1.r) - obj.x) <= 10:
                    #print("coin")
                    obj.coincol()

        self.intructions.update()







    def on_key_press(self, symbol, modifiers: int):
        print(symbol)
        self.player1.control(symbol)
        if symbol == 114:
            for i in self.worldlist:
                i.reset()



    # def on_key_release(self, symbol: int, modifiers: int):
    #     print(symbol)
    #     for box in self.box_list:
    #         box.stop(symbol)

def main():
    mywindow = MyGame(SW, SH, "User Control")
    arcade.run()


if __name__ == "__main__":
    main()