import copy

from position import Position
from position_generator import PositionGenerator
from game import Game
from doubles import allow


class TestGame:
    def setup(self):
        self.defaut_position_generator = PositionGenerator()
        allow(self.defaut_position_generator).get_position.and_return(Position(0, 0))

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
        game = Game(10, self.defaut_position_generator)
        game.initialize_snake()
        game.snake.position = Position(8, 8)
        game.place_nugget_at_position(Position(1, 1))

        game.update()

        nugget = game.get_nugget()
        assert Position(1, 1) == nugget.position

    def test_when_snake_eats_nugget_then_tail_grows(self):
        position_generator = PositionGenerator()
        allow(position_generator).get_position.and_return(None)
        game = Game(10, position_generator)
        game.initialize_snake()
        game.snake.position = Position(5, 5)
        game.snake.orientation = 'down'
        game.place_nugget_at_position(Position(5, 4))

        game.update()

        tail = game.get_snake_tail()
        assert 1 == len(tail)
        assert Position(5, 5) == tail[0]

    def test_when_snake_dies_then_respawn_in_initial_position(self):
        game = Game(10, self.defaut_position_generator)
        game.initialize_snake()
        initial_position = copy.deepcopy(game.snake.position)
        game.snake.position = None

        game.die()

        assert initial_position == game.snake.position

    def test_when_snake_dies_then_reset_tail_to_initial_length(self):
        game = Game(10, self.defaut_position_generator)
        game.initialize_snake()
        initial_length = len(game.snake.tail)
        game.snake.tail = [
            Position(5, 6),
            Position(6, 6),
            Position(6, 5),
            Position(6, 4),
            Position(5, 4)
        ]

        game.die()

        assert initial_length == len(game.snake.tail)

    def test_when_snake_dies_then_respawn_nugget(self):
        position_generator = PositionGenerator()
        allow(position_generator).get_position.and_return(Position(2, 2), Position(3, 3))
        game = Game(10, position_generator)
        game.place_nugget()
        assert Position(2, 2) == game.nugget.position

        game.die()

        assert Position(3, 3) == game.nugget.position
