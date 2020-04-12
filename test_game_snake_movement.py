from doubles import allow

from game import Game
from position import Position
from position_generator import PositionGenerator


class TestGameSnakeMovement:
    def setup(self):
        self.defaut_position_generator = PositionGenerator()
        allow(self.defaut_position_generator).get_position.and_return(Position(0, 0))

    def test_when_snake_initialized_then_snake_is_in_the_middle(self):
        game = Game(10)
        game.initialize_snake()
        assert Position(5, 5) == game.snake.position

    def test_given_odd_map_size_when_snake_initialized_then_snake_is_in_the_middle(self):
        game = Game(9)
        game.initialize_snake()
        assert Position(4, 4) == game.snake.position

    def test_when_snake_initialized_then_snake_is_facing_down(self):
        game = Game(10)
        game.initialize_snake()
        assert 'down' == game.snake.orientation

    def test_when_update_while_facing_down_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('down')
        game.update()
        assert Position(5, 4) == game.snake.position

    def test_when_update_while_facing_up_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('up')
        game.update()
        assert Position(5, 6) == game.snake.position

    def test_when_update_while_facing_left_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('left')
        game.update()
        assert Position(4, 5) == game.snake.position

    def test_when_update_while_facing_right_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('right')
        game.update()
        assert Position(6, 5) == game.snake.position

    def test_when_requesting_orientation_to_the_sides_then_snake_turns(self):
        game = Game(10)
        game.initialize_snake()

        game.snake.set_orientation('down')
        game.request_orientation('left')
        assert 'left' == game.snake.orientation

        game.snake.set_orientation('down')
        game.request_orientation('right')
        assert 'right' == game.snake.orientation

        game.snake.set_orientation('up')
        game.request_orientation('left')
        assert 'left' == game.snake.orientation

        game.snake.set_orientation('up')
        game.request_orientation('right')
        assert 'right' == game.snake.orientation

        game.snake.set_orientation('left')
        game.request_orientation('up')
        assert 'up' == game.snake.orientation

        game.snake.set_orientation('left')
        game.request_orientation('down')
        assert 'down' == game.snake.orientation

        game.snake.set_orientation('right')
        game.request_orientation('up')
        assert 'up' == game.snake.orientation

        game.snake.set_orientation('right')
        game.request_orientation('down')
        assert 'down' == game.snake.orientation

    def test_when_requesting_orientation_backwards_then_snake_doesnt_turn(self):
        game = Game(10)
        game.initialize_snake()

        game.snake.set_orientation('down')
        game.request_orientation('up')
        assert 'down' == game.snake.orientation

        game.snake.set_orientation('up')
        game.request_orientation('down')
        assert 'up' == game.snake.orientation

        game.snake.set_orientation('right')
        game.request_orientation('left')
        assert 'right' == game.snake.orientation

        game.snake.set_orientation('left')
        game.request_orientation('right')
        assert 'left' == game.snake.orientation

    def test_when_snake_hits_wall_then_snake_dies(self):
        game = Game(1, self.defaut_position_generator)
        game.initialize_snake()

        game.snake.position = Position(0, 0)
        game.snake.orientation = 'down'
        game.update()
        assert 1 == game.deaths

        game.snake.position = Position(0, 0)
        game.snake.orientation = 'right'
        game.update()
        assert 2 == game.deaths

        game.snake.position = Position(0, 0)
        game.snake.orientation = 'up'
        game.update()
        assert 3 == game.deaths

        game.snake.position = Position(0, 0)
        game.snake.orientation = 'left'
        game.update()
        assert 4 == game.deaths

    def test_when_snake_hits_its_tail_then_it_dies(self):
        game = Game(10, self.defaut_position_generator)
        game.initialize_snake()
        game.snake.tail = [
            Position(5, 6),
            Position(6, 6),
            Position(6, 5),
            Position(6, 4),
            Position(5, 4)
        ]

        game.update()

        assert 1 == game.deaths
