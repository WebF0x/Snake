from nugget import Nugget
from position import Position
from snake import Snake


class Game:
    def __init__(self, map_size, position_generator=None):
        self.deaths = 0
        self.map_size = map_size
        self.snake = None
        self.nugget = None
        self.position_generator = position_generator

    def initialize_snake(self):
        self.snake = Snake(
            Position(self.map_size // 2, self.map_size // 2),
            orientation='down'
        )
        self.snake.eat(2)

    def update(self):
        self.move_snake_forward()
        self.check_nugget_collision()
        self.check_wall_collision()
        self.check_tail_collision()

    def check_tail_collision(self):
        if self.snake.position in self.snake.tail:
            self.die()

    def check_wall_collision(self):
        if (self.snake.position.x == -1 or
                self.snake.position.y == -1 or
                self.snake.position.x == self.map_size or
                self.snake.position.y == self.map_size):
            self.die()

    def die(self):
        self.deaths += 1
        self.reset()

    def reset(self):
        self.initialize_snake()
        self.place_nugget()

    def check_nugget_collision(self):
        if not self.nugget:
            return
        if self.snake.position == self.nugget.position:
            self.place_nugget()
            self.snake.eat()

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

    def get_snake_tail(self):
        return self.snake.tail

    def move_snake_forward(self):
        self.snake.move()
