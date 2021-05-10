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

import arcade
import random


# --- Constants ---
SW = 1500
SH = 800
SP = 20
pilot_scale = 0.11
reaper_scale = 0.3
r_count = 10

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("srs_helmet.png", pilot_scale)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        elif self.right > SW:
            self.right = SW
        if self.bottom < 0:
            self.bottom = 0
        if self.top > SH:
            self.top = SH

class Reaper(arcade.Sprite):
    def __init__(self):
        super().__init__("TF2_Reaper.png", reaper_scale)
        self.dx = random.randrange(2, 10, 1)
        self.dy = random.randrange(2, 10, 1)

    def update(self):
        self.center_y += self.dy
        self.center_x += self.dx

        if self.top > SH or self.bottom < 0:
            self.dy *= -1
        elif self.right > SW or self.left < 0:
            self.dx *= -1


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.load_texture("galaxy.jpg")
        self.total_time = 0.0
        self.set_mouse_platform_visible(False)

    def reset(self):
        self.player_list = arcade.SpriteList()
        self.reaper_list = arcade.SpriteList()
        self.gameover = False

        self.total_time = 0.0

        self.pilot = Player()
        self.pilot.center_x = SW / 2
        self.pilot.center_y = SH / 2
        self.player_list.append(self.pilot)

        for i in range(r_count):
            self.reaper = Reaper()
            self.reaper.center_x = random.randrange(self.reaper.width // 2, SW - self.reaper.width // 2)
            self.reaper.center_y = random.randrange(self.reaper.height // 2, SH - self.reaper.height // 2)
            self.reaper_list.append(self.reaper)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SW // 2, SH // 2, SW, SH, self.background)
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        self.player_list.draw()
        self.reaper_list.draw()

        objective = "Current Objective: Survive for 1 minute"
        t_output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(objective, SW/2, SH - 40, arcade.color.VIOLET_BLUE, 20)
        arcade.draw_text(t_output, SW / 2, SH - 70, arcade.color.VIOLET_BLUE, 20)





        if self.gameover == True:
            arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Game Over: Press P to Play Again!", SW / 2 - 50, SH / 2 - 20, ((0, 255, 0)), 14)



    def on_update(self, dt):
        self.player_list.update()
        self.reaper_list.update()
        self.total_time += dt

        pilot_hit = arcade.check_for_collision_with_list(self.pilot, self.reaper_list)
        if len(pilot_hit) > 0:
            self.pilot.kill()
            self.gameover = True

        if self.total_time > 61.0 and not self.gameover:
            self.gameover = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.pilot.change_x = -SP
        elif key == arcade.key.D:
            self.pilot.change_x = SP
        elif key == arcade.key.W:
            self.pilot.change_y = SP
        elif key == arcade.key.S:
            self.pilot.change_y = -SP
        elif key == arcade.key.P:
            self.reset()



    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.pilot.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.pilot.change_y = 0


# -----Main Function--------
def main():
    window = MyGame(SW, SH, "GAME TEST")
    window.reset()
    arcade.run()


# ------Run Main Function-----
if __name__ == "__main__":
    main()
