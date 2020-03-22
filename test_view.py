from view import get_head_vertices


class TestView():
    def test_get_head_vertices_facing_up(self):
        canvas = {
            'x': 20,
            'y': 10,
            'width': 200,
            'height': 100
        }
        orientation = 'up'
        vertices = get_head_vertices(canvas, orientation)
        left_cheek = {'x': 20, 'y': 10}
        right_cheek = {'x': 220, 'y': 10}
        mouth = {'x': 120, 'y': 110}
        assert right_cheek in vertices
        assert left_cheek in vertices
        assert mouth in vertices

    def test_get_head_vertices_facing_down(self):
        canvas = {
            'x': 20,
            'y': 10,
            'width': 200,
            'height': 100
        }
        orientation = 'down'
        vertices = get_head_vertices(canvas, orientation)
        left_cheek = {'x': 20, 'y': 110}
        right_cheek = {'x': 220, 'y': 110}
        mouth = {'x': 120, 'y': 10}
        assert right_cheek in vertices
        assert left_cheek in vertices
        assert mouth in vertices

    def test_get_head_vertices_facing_right(self):
        canvas = {
            'x': 20,
            'y': 10,
            'width': 200,
            'height': 100
        }
        orientation = 'right'
        vertices = get_head_vertices(canvas, orientation)
        left_cheek = {'x': 20, 'y': 10}
        right_cheek = {'x': 20, 'y': 110}
        mouth = {'x': 220, 'y': 60}
        assert right_cheek in vertices
        assert left_cheek in vertices
        assert mouth in vertices

    def test_get_head_vertices_facing_left(self):
        canvas = {
            'x': 20,
            'y': 10,
            'width': 200,
            'height': 100
        }
        orientation = 'left'
        vertices = get_head_vertices(canvas, orientation)
        left_cheek = {'x': 220, 'y': 110}
        right_cheek = {'x': 220, 'y': 10}
        mouth = {'x': 20, 'y': 60}
        assert right_cheek in vertices
        assert left_cheek in vertices
        assert mouth in vertices
