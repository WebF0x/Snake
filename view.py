import arcade


def get_head_vertices(canvas, orientation):
    left = canvas['x']
    right = left + canvas['width']
    bottom = canvas['y']
    top = bottom + canvas['height']
    middle_horizontal = left + canvas['width'] / 2
    middle_vertical = bottom + canvas['height'] / 2

    left_cheek = None
    right_cheek = None
    mouth = None

    if orientation == 'down':
        left_cheek = {'x': right, 'y': top}
        right_cheek = {'x': left, 'y': top}
        mouth = {'x': middle_horizontal, 'y': bottom}
    elif orientation == 'up':
        left_cheek = {'x': left, 'y': bottom}
        right_cheek = {'x': right, 'y': bottom}
        mouth = {'x': middle_horizontal, 'y': top}
    elif orientation == 'right':
        left_cheek = {'x': left, 'y': top}
        right_cheek = {'x': left, 'y': bottom}
        mouth = {'x': right, 'y': middle_vertical}
    elif orientation == 'left':
        left_cheek = {'x': right, 'y': bottom}
        right_cheek = {'x': right, 'y': top}
        mouth = {'x': left, 'y': middle_vertical}

    return [left_cheek, right_cheek, mouth]


def draw_snake_head(canvas, orientation):
    vertices = get_head_vertices(canvas, orientation)
    for i, vertex in enumerate(vertices):
        next_vertex = vertices[(i + 1) % len(vertices)]
        arcade.draw_line(
            vertex['x'],
            vertex['y'],
            next_vertex['x'],
            next_vertex['y'],
            arcade.color.BLACK,
            1
        )


def draw_nugget(canvas):
    half_width = canvas['width'] / 2
    half_height = canvas['height'] / 2
    arcade.draw_circle_outline(
        center_x=canvas['x'] + half_width,
        center_y=canvas['y'] + half_height,
        radius=min(half_width, half_height),
        color=arcade.color.RED,
    )
