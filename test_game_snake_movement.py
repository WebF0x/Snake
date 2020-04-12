from game import Game
from position import Position


class TestGameSnakeMovement:
    def test_when_snake_initialized_then_snake_is_in_the_middle_facing(self):
        game = Game(10)
        game.initialize_snake()
        assert Position(5, 5) == game.snake.position

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
