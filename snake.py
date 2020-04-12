import copy


class Snake:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation
        self.tail = []
        self.food = 0

    def set_orientation(self, orientation):
        self.orientation = orientation

    def grow_tail(self):
        self.tail.insert(0, self.get_neck_position())
        self.food -= 1

    def get_neck_position(self):
        neck_position = copy.deepcopy(self.position)
        if self.orientation == 'down':
            neck_position.y += 1
            return neck_position
        if self.orientation == 'up':
            neck_position.y -= 1
            return neck_position
        if self.orientation == 'right':
            neck_position.x -= 1
            return neck_position
        if self.orientation == 'left':
            neck_position.x += 1
            return neck_position

    def move(self):
        self.move_head()
        if self.food != 0:
            self.grow_tail()
            return
        self.move_tail()

    def move_head(self):
        if self.orientation == 'down':
            self.position.y -= 1
        elif self.orientation == 'up':
            self.position.y += 1
        elif self.orientation == 'left':
            self.position.x -= 1
        elif self.orientation == 'right':
            self.position.x += 1

    def move_tail(self):
        if not self.tail:
            return
        self.tail.pop()
        self.tail.insert(0, self.get_neck_position())

    def eat(self, amount=1):
        self.food += amount
