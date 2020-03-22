from snake import Snake


class Game:
    def __init__(self, map_size):
        self.map_size = map_size
        self.snake = None

    def initialize_snake(self):
        self.snake = Snake(
            x=self.map_size / 2,
            y=self.map_size / 2,
            orientation='down'
        )

    def update(self):
        if self.snake.orientation == 'down':
            self.snake.y -= 1
        elif self.snake.orientation == 'up':
            self.snake.y += 1
        elif self.snake.orientation == 'left':
            self.snake.x -= 1
        elif self.snake.orientation == 'right':
            self.snake.x += 1
