import arcade

from snake import Snake
from view import draw_snake_head

CELL_SIZE_PIXELS = 10
MAP_SIZE_CELLS = 50
MAP_SIZE_PIXELS = MAP_SIZE_CELLS * CELL_SIZE_PIXELS
SNAKE_START_POSITION = {'x': MAP_SIZE_CELLS/2, 'y': MAP_SIZE_CELLS/2}

arcade.open_window(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS, "Snake")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

snake = Snake(SNAKE_START_POSITION['x'], SNAKE_START_POSITION['y'], 'down')
snake_head_canvas = {
    'x': snake.x * CELL_SIZE_PIXELS,
    'y': snake.y * CELL_SIZE_PIXELS,
    'width': CELL_SIZE_PIXELS,
    'height': CELL_SIZE_PIXELS
}
draw_snake_head(snake_head_canvas, snake.orientation)

arcade.finish_render()
arcade.run()
