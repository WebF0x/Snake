from view import View


class TestView:
    def setup(self):
        self.view = View()

    def test_sprite_scaling_to_canvas_horizontally(self):
        canvas = {
            'x': 0,
            'y': 0,
            'width': 10,
            'height': 20
        }

        class SpriteStub:
            def __init__(self):
                self.width = 5
                self.height = 1
        sprite = SpriteStub()

        assert 2 == self.view.get_sprite_scaling(canvas, sprite)

    def test_sprite_scaling_to_canvas_vertically(self):
        canvas = {
            'x': 0,
            'y': 0,
            'width': 10,
            'height': 20
        }

        class SpriteStub:
            def __init__(self):
                self.width = 1
                self.height = 4
        sprite = SpriteStub()

        assert 5 == self.view.get_sprite_scaling(canvas, sprite)
