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

haha get the cs
click the minion when its health is low
if you do it good then you get money

when a minion is clicked, subtract a certain amount of health from that minion
if the minions health drops to or below zero then it will die
if it dies from a user's click, then give the player gold/cs
'''

import arcade
import random


class Crosshair:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw_crosshair(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size / 5, self.color)
        arcade.draw_rectangle_filled(self.x, self.y, self.size / 5, self.size, self.color)


class Minion:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.size = 50
        self.image = arcade.Sprite("melee_Minion.png", .2)
        self.image.center_x = x
        self.image.center_y = y

    def draw_minion(self):
        self.image.draw()
        arcade.draw_text(str(self.health), self.x, self.y + 20, arcade.color.BLACK)

    def update_minion(self):
        if random.randint(1, 11) == 1:
            self.health -= 10


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)
        self.auto_sound = arcade.load_sound("laser.mp3")

        self.crosshair = Crosshair(100, 100, 20, arcade.color.RED)

        self.cs_counter = 0
        self.auto_damage = 87

        self.minion_list = []
        for i in range(6):
            if i % 2 == 1:  # if the range is an odd number
                self.minion_list.append(Minion(130 * i, 450, 600))
            else:
                self.minion_list.append(Minion(130 + (130 * i), 180, 600))

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.minion_list)):      # create all of the minions in the list
            self.minion_list[i].draw_minion()

        self.crosshair.draw_crosshair()     # draw the crosshair
        arcade.draw_text("CS: "+str(self.cs_counter), 710, 570, arcade.color.BLACK, font_size=20)  # draw the cs counter
        arcade.draw_text("DMG: "+str(self.auto_damage), 30, 570, arcade.color.BLACK, font_size=20)

    def on_update(self, delta_time: float):
        for i in range(len(self.minion_list)):      # update all of the minions
            self.minion_list[i].update_minion()

            if self.minion_list[i].health <= 0:     # if a minion dies then copy it and replace it
                self.minion_list[i].health += 600

        self.auto_damage = 87 + (self.cs_counter * 1 / 2)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.crosshair.x = x
        self.crosshair.y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for i in range(len(self.minion_list)):      # if the crosshair is on top of one of the minions
            if (self.crosshair.x >= self.minion_list[i].x - 80) and (self.crosshair.x <= self.minion_list[i].x + 80) \
                    and (self.crosshair.y >= self.minion_list[i].y - 80) and (self.crosshair.y <= self.minion_list[i].y + 80):
                self.minion_list[i].health -= self.auto_damage       # then remove health from it
                arcade.play_sound(self.auto_sound)
                if self.minion_list[i].health <= 0:
                    self.cs_counter += 1            # if the minion dies from the click, then add 1 to cs counter


def main():
    window = Render(800, 600, 'CS')
    arcade.run()


if __name__ == '__main__':
    main()
