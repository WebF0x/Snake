from copy import deepcopy

import arcade


class View:
    def __init__(self):
        self.sprite_rabbit = None
        self.sprite_easter_egg = None
        self.sprite_chick = None

    def load_images(self):
        self.sprite_rabbit = arcade.Sprite('images/bunny.jpg')
        self.sprite_easter_egg = arcade.Sprite('images/easter_egg.png')
        self.sprite_chick = arcade.Sprite('images/chick.png')

    def draw_snake_head(self, canvas):
        self.draw_sprite(canvas, self.sprite_rabbit)

    def draw_nugget(self, canvas):
        self.draw_sprite(canvas, self.sprite_easter_egg)

    def draw_snake_tail_segment(self, canvas):
        self.draw_sprite(canvas, self.sprite_chick)

    def draw_sprite(self, canvas, source_sprite):
        sprite = deepcopy(source_sprite)
        sprite.center_x = canvas['x'] + canvas['width'] / 2
        sprite.center_y = canvas['y'] + canvas['height'] / 2
        sprite.scale = self.get_sprite_scaling(canvas, sprite)
        sprite.draw()

    @staticmethod
    def get_sprite_scaling(canvas, sprite):
        potential_scaling_horizontal = canvas['width'] / sprite.width
        potential_scaling_vertical = canvas['height'] / sprite.height
        return min(potential_scaling_horizontal, potential_scaling_vertical)
