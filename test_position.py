from position import Position


class TestPosition:
    def test_equality(self):
        assert Position(1, 2) == Position(1, 2)

    def test_inequality(self):
        assert Position(1, 2) != Position(3, 4)
        assert Position(1, 1) != Position(1, 2)
        assert Position(1, 1) != Position(2, 1)
