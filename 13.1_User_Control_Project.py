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

sw = 600
sh = 600
gold_speed = 1
gold_scale = .1
gold_count = 50
player_scale = .3
player_speed = 5


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("player.png", player_scale)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= sw:
            self.right = sw
        elif self.left <= 0:
            self.left = 0
        elif self.top > sh:
            self.top = sh
        elif self.bottom <= 0:
            self.bottom = 0


class Gold(arcade.Sprite):
    def __init__(self):
        super().__init__("gold_ingot.png", gold_scale)
        self.w = int(self.width)
        self.h = int(self.height)

    def update(self):
        self.center_y -= gold_speed
        if self.top < 0:
            self.center_x = random.randrange(self.w, sw - self.w)
            self.center_y = random.randrange(sh + self.h, sh * 2)


class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        self.set_mouse_visible(False)
        self.background = None
        self.background = arcade.load_texture("background_image.jpg")

    def reset(self):
        self.gold_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.score = 0
        self.Gameover = False

        # create player
        self.player = Player()
        self.player.center_x = sw / 2
        self.player.center_y = 30
        self.player_list.append(self.player)

        # create gold
        for i in range(gold_count):
            gold = Gold()
            gold.center_x = random.randrange(gold.w//2, sw-gold.w//2)
            gold.center_y = random.randrange(sh//2, sh*2)
            self.gold_list.append(gold)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, sw, sh, self.background)
        self.player_list.draw()
        self.gold_list.draw()
        the_score = f"Score:{self.score}"
        arcade.draw_text(the_score, sw-80, sh-20, arcade.color.WHITE, 14)

        gold_left = f"Gold left:{len(self.gold_list)}"
        arcade.draw_text(gold_left, 10, 40, arcade.color.BLACK, 14)

        if self.Gameover == True:
            arcade.draw_rectangle_filled(sw // 2, sh // 2, sw, sh, arcade.color.BLACK)
            arcade.draw_text("Game Over:Press Space to Play Again", sw/2, sh/2-20, ((0, 255, 0)), 14, align="center",
                             anchor_x="center")


    def on_update(self, dt):
        self.player_list.update()
        self.gold_list.update()

        if len(self.gold_list) == 0:
            self.Gameover = True

        gold_hit_list = arcade.check_for_collision_with_list(self.player, self.gold_list)
        for gold in gold_hit_list:
            gold.kill()
            self.score += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -player_speed
        elif key == arcade.key.RIGHT:
            self.player.change_x = player_speed
        elif key == arcade.key.UP:
            self.player.change_y = player_speed
        elif key == arcade.key.DOWN:
            self.player.change_y = -player_speed
        elif key == arcade.key.SPACE:
            self.reset()



    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    my_window = MyGame(sw, sh, "mouse control")
    my_window.reset()
    arcade.run()


if __name__ == "__main__":
    main()
