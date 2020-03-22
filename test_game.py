from game import Game


class TestGame():
    def test_when_snake_initialized_then_snake_is_in_the_middle_facing(self):
        game = Game(10)
        game.initialize_snake()
        assert 5 == game.snake.x
        assert 5 == game.snake.y

    def test_when_snake_initialized_then_snake_is_facing_down(self):
        game = Game(10)
        game.initialize_snake()
        assert 'down' == game.snake.orientation

    def test_when_update_while_facing_down_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('down')
        game.update()
        assert 5 == game.snake.x
        assert 4 == game.snake.y

    def test_when_update_while_facing_up_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('up')
        game.update()
        assert 5 == game.snake.x
        assert 6 == game.snake.y

    def test_when_update_while_facing_left_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('left')
        game.update()
        assert 4 == game.snake.x
        assert 5 == game.snake.y

    def test_when_update_while_facing_right_then_snake_moves_forward(self):
        game = Game(10)
        game.initialize_snake()
        game.snake.set_orientation('right')
        game.update()
        assert 6 == game.snake.x
        assert 5 == game.snake.y
