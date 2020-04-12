from nugget import Nugget
from position import Position
from snake import Snake


class Game:
    def __init__(self, map_size, position_generator=None):
        self.map_size = map_size
        self.snake = None
        self.nugget = None
        self.position_generator = position_generator

    def initialize_snake(self):
        self.snake = Snake(
            Position(self.map_size / 2, self.map_size / 2),
            orientation='down'
        )

    def update(self):
        if self.snake.orientation == 'down':
            self.snake.position.y -= 1
        elif self.snake.orientation == 'up':
            self.snake.position.y += 1
        elif self.snake.orientation == 'left':
            self.snake.position.x -= 1
        elif self.snake.orientation == 'right':
            self.snake.position.x += 1

    def request_orientation(self, requested_orientation):
        current_orientation = self.snake.orientation

        if current_orientation == 'up' and requested_orientation == 'down':
            return
        if current_orientation == 'down' and requested_orientation == 'up':
            return
        if current_orientation == 'left' and requested_orientation == 'right':
            return
        if current_orientation == 'right' and requested_orientation == 'left':
            return

        self.snake.set_orientation(requested_orientation)

    def place_nugget_at_position(self, position):
        self.nugget = Nugget(position)

    def place_nugget(self):
        position = self.position_generator.get_position()
        self.place_nugget_at_position(position)

    def get_nugget(self):
        return self.nugget
