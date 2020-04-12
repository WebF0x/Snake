import random
import sys
import traceback

import arcade

from game import Game
from position import Position
from random_position_generator import RandomPositionGenerator
from view import View

FRAME_PERIOD = 0.2

CELL_SIZE_PIXELS = 40
MAP_SIZE_CELLS = 20
MAP_SIZE_PIXELS = MAP_SIZE_CELLS * CELL_SIZE_PIXELS


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS, "Snake")
        arcade.set_background_color(arcade.color.WHITE)
        self.game = None
        self.time_since_last_frame = 0
        self.view = View()

    def setup(self):
        self.view.load_images()
        random.seed()
        random_number_generator = random.Random()
        random_position_generator = RandomPositionGenerator(random_number_generator, MAP_SIZE_CELLS-1)
        self.game = Game(MAP_SIZE_CELLS, random_position_generator)
        self.game.place_nugget()
        self.game.initialize_snake()

    def on_update(self, delta_time):
        self.time_since_last_frame += delta_time
        if self.time_since_last_frame >= FRAME_PERIOD:
            self.game.update()
            self.time_since_last_frame -= FRAME_PERIOD

    def on_draw(self):
        try:
            self.draw()
        except Exception:
            print('Error while drawing the game', file=sys.stderr)
            traceback.print_exc()
            exit(1)

    def draw(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()
        if self.game.nugget:
            nugget_canvas = self.get_canvas_from_cell(self.game.nugget.position)
            self.view.draw_nugget(nugget_canvas)
        snake_head_canvas = self.get_canvas_from_cell(Position(self.game.snake.position.x, self.game.snake.position.y))
        self.view.draw_snake_head(snake_head_canvas)
        self.draw_snake_tail()

    def draw_snake_tail(self):
        for segment in self.game.get_snake_tail():
            canvas = self.get_canvas_from_cell(segment)
            self.view.draw_snake_tail_segment(canvas)

    @staticmethod
    def get_canvas_from_cell(position):
        return {
            'x': position.x * CELL_SIZE_PIXELS,
            'y': position.y * CELL_SIZE_PIXELS,
            'width': CELL_SIZE_PIXELS,
            'height': CELL_SIZE_PIXELS
        }

    def on_key_press(self, symbol, modifiers):
        requested_orientation = None
        if symbol == arcade.key.DOWN:
            requested_orientation = 'down'
        elif symbol == arcade.key.UP:
            requested_orientation = 'up'
        elif symbol == arcade.key.LEFT:
            requested_orientation = 'left'
        elif symbol == arcade.key.RIGHT:
            requested_orientation = 'right'

        if requested_orientation:
            self.game.request_orientation(requested_orientation)


def main():
    window = GameWindow()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
