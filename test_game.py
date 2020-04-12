from position import Position
from position_generator import PositionGenerator
from game import Game
from doubles import allow


class TestGame:
    def test_when_snake_initialized_then_snake_is_in_the_middle_facing(self):
        game = Game(10)
        game.initialize_snake()
        assert 5 == game.snake.position.x
        assert 5 == game.snake.position.y

    def test_when_snake_initialized_then_snake_is_facing_down(self):
        game = Game(10)
        game.initialize_snake()
        assert 'down' == game.snake.orientation

    def test_when_update_while_facing_down_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('down')
        game.update()
        assert 5 == game.snake.position.x
        assert 4 == game.snake.position.y

    def test_when_update_while_facing_up_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('up')
        game.update()
        assert 5 == game.snake.position.x
        assert 6 == game.snake.position.y

    def test_when_update_while_facing_left_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('left')
        game.update()
        assert 4 == game.snake.position.x
        assert 5 == game.snake.position.y

    def test_when_update_while_facing_right_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('right')
        game.update()
        assert 6 == game.snake.position.x
        assert 5 == game.snake.position.y

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

    def test_place_nugget(self):
        game = Game(10)

        game.place_nugget_at_position(Position(5, 10))

        nugget = game.get_nugget()
        assert 5 == nugget.position.x
        assert 10 == nugget.position.y

    def test_place_nugget_at_random_place(self):
        position_generator = PositionGenerator()
        allow(position_generator).get_position.and_return(Position(5, 10))
        game = Game(10, position_generator)

        game.place_nugget()

        nugget = game.get_nugget()
        assert 5 == nugget.position.x
        assert 10 == nugget.position.y
