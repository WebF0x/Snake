from doubles import allow

from game import Game
from position import Position
from position_generator import PositionGenerator


class TestGameNugget:
    def test_place_nugget(self):
        game = Game(10)

        game.place_nugget_at_position(Position(5, 10))

        nugget = game.get_nugget()
        assert Position(5, 10) == nugget.position

    def test_place_nugget_at_random_place(self):
        position_generator = PositionGenerator()
        allow(position_generator).get_position.and_return(Position(5, 10))
        game = Game(10, position_generator)

        game.place_nugget()

        nugget = game.get_nugget()
        assert Position(5, 10) == nugget.position
