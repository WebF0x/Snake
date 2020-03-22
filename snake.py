import arcade

from view import draw_snake_head

CELL_SIZE_PIXELS = 10
MAP_SIZE_CELLS = 50
MAP_SIZE_PIXELS = MAP_SIZE_CELLS * CELL_SIZE_PIXELS
SNAKE_START_POSITION = {'x': MAP_SIZE_CELLS/2, 'y': MAP_SIZE_CELLS/2}

arcade.open_window(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS, "Snake")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

snake_head_canvas = {
    'x': SNAKE_START_POSITION['x'] * CELL_SIZE_PIXELS,
    'y': SNAKE_START_POSITION['y'] * CELL_SIZE_PIXELS,
    'width': CELL_SIZE_PIXELS,
    'height': CELL_SIZE_PIXELS
}
draw_snake_head(snake_head_canvas, 'down')

arcade.finish_render()
arcade.run()
