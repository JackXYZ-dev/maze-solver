from window import Point, Line


class Cell:
    def __init__(
        self,
        has_left_wall,
        has_right_wall,
        has_top_wall,
        has_bottom_wall,
        x1,
        x2,
        y1,
        y2,
        win,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        # Corners
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            left_wall.draw(self._win, "black")
        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            right_wall.draw(self._win, "black")
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            top_wall.draw(self._win, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            bottom_wall.draw(self._win, "black")
