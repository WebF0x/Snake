from position import Position
from position_generator import PositionGenerator
from game import Game
from doubles import allow


class TestGame:
    def test_when_snake_eats_nugget_then_nugget_spawns_elsewhere(self):
        position_generator = PositionGenerator()
        allow(position_generator).get_position.and_return(Position(2, 2))
        game = Game(10, position_generator)
        game.initialize_snake()
        game.snake.set_orientation('down')
        game.snake.position = Position(1, 2)
        game.place_nugget_at_position(Position(1, 1))

        game.update()

        nugget = game.get_nugget()
        assert Position(2, 2) == nugget.position

    def test_when_snake_doesnt_eat_nugget_then_nugget_doesnt_move(self):
        game = Game(10, None)
        game.initialize_snake()
        game.snake.position = Position(8, 8)
        game.place_nugget_at_position(Position(1, 1))

        game.update()

        nugget = game.get_nugget()
        assert Position(1, 1) == nugget.position
