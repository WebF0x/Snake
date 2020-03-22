import arcade

from game import Game
from view import draw_snake_head

FRAME_PERIOD = 0.2

CELL_SIZE_PIXELS = 15
MAP_SIZE_CELLS = 50
MAP_SIZE_PIXELS = MAP_SIZE_CELLS * CELL_SIZE_PIXELS


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS, "Snake")
        arcade.set_background_color(arcade.color.WHITE)
        self.game = None
        self.time_since_last_frame = 0

    def setup(self):
        self.game = Game(MAP_SIZE_CELLS)
        self.game.initialize_snake()

    def on_update(self, delta_time):
        self.time_since_last_frame += delta_time
        if self.time_since_last_frame >= FRAME_PERIOD:
            self.game.update()
            self.time_since_last_frame -= FRAME_PERIOD

    def on_draw(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()
        snake_head_canvas = {
            'x': self.game.snake.x * CELL_SIZE_PIXELS,
            'y': self.game.snake.y * CELL_SIZE_PIXELS,
            'width': CELL_SIZE_PIXELS,
            'height': CELL_SIZE_PIXELS
        }
        draw_snake_head(snake_head_canvas, self.game.snake.orientation)

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
