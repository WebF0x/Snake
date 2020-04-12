from position import Position
from snake import Snake


class TestSnake:
    def test_get_neck_position(self):
        snake = Snake(Position(5, 5), 'down')

        snake.set_orientation('down')
        assert Position(5, 6) == snake.get_neck_position()

        snake.set_orientation('up')
        assert Position(5, 4) == snake.get_neck_position()

        snake.set_orientation('right')
        assert Position(4, 5) == snake.get_neck_position()

        snake.set_orientation('left')
        assert Position(6, 5) == snake.get_neck_position()

    def test_when_snake_moves_then_tail_follows(self):
        snake = Snake(Position(5, 5), 'down')
        snake.tail = [
            Position(5, 6),
            Position(5, 7),
            Position(4, 7),
            Position(4, 8)
        ]

        snake.move()

        assert 4 == len(snake.tail)
        assert Position(5, 5) == snake.tail[0]
        assert Position(5, 6) == snake.tail[1]
        assert Position(5, 7) == snake.tail[2]
        assert Position(4, 7) == snake.tail[3]

    def test_when_snake_has_food_and_moves_then_tail_grows_by_one_segment(self):
        snake = Snake(Position(5, 5), 'down')
        snake.tail = [
            Position(5, 6),
            Position(5, 7),
            Position(4, 7)
        ]
        snake.eat()
        assert 3 == len(snake.tail)
        snake.eat()
        assert 3 == len(snake.tail)

        snake.move()
        assert 4 == len(snake.tail)
        snake.move()
        assert 5 == len(snake.tail)

    def test_when_snake_has_no_food_and_moves_then_tail_doesnt_grow(self):
        snake = Snake(Position(5, 5), 'down')
        snake.tail = [
            Position(5, 6),
            Position(5, 7),
            Position(4, 7)
        ]
        snake.eat()
        snake.move()
        assert 4 == len(snake.tail)

        snake.move()

        assert 4 == len(snake.tail)

    def test_when_tail_grows_then_new_tail_segment_is_at_the_neck(self):
        snake = Snake(Position(5, 5), 'down')
        snake.tail = [
            Position(5, 6),
            Position(5, 7),
            Position(4, 7)
        ]

        snake.eat()
        snake.move()

        assert snake.get_neck_position() == snake.tail[0]

    def test_when_tail_grows_then_tip_of_tail_doesnt_move(self):
        snake = Snake(Position(5, 5), 'down')
        snake.tail = [
            Position(5, 6),
            Position(5, 7),
            Position(4, 7)
        ]

        snake.eat()
        snake.move()

        assert Position(4, 7) == snake.tail[-1]
