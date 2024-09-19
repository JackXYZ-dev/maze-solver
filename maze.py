from cell import Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.seed = seed

        if self.seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for i, col_cells in enumerate(self._cells):
            for j, cell in enumerate(col_cells):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + (i * self.cell_size_x)
        x2 = x1 + self.cell_size_x
        y1 = self._y1 + (j * self.cell_size_y)
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        # The entrance to the maze will always be at the top of the top-left cell,
        # the exit always at the bottom of the bottom-right cell.

        first_cell = self._cells[0][0]
        last_cell = self._cells[len(self._cells) - 1][len(self._cells[0]) - 1]

        first_cell.has_top_wall = False
        last_cell.has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check the cells that are directly adjacent to the current cell.
            # Above cell
            if j > 0:
                above_cell = self._cells[i][j - 1]
                if above_cell.visited == False:
                    to_visit.append((i, j - 1))
            # Right cell
            if i < len(self._cells[0]) - 1:
                right_cell = self._cells[i + 1][j]
                if right_cell.visited == False:
                    to_visit.append((i + 1, j))
            # Below cell
            if j < len(self._cells) - 1:
                below_cell = self._cells[i][j + 1]
                if below_cell.visited == False:
                    to_visit.append((i, j + 1))
            # Left cell
            if i > 0:
                left_cell = self._cells[i - 1][j]
                if left_cell.visited == False:
                    to_visit.append((i - 1, j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                next_i, next_j = to_visit[random.randrange(len(to_visit))]
                current_cell = self._cells[i][j]
                next_cell = self._cells[next_i][next_j]
                # Moving up
                if next_j == j - 1:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                # Moving right
                if next_i == i + 1:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                # Moving down
                if next_j == j + 1:
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                # Moving left
                if next_i == i - 1:
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False

                current_cell.draw()
                next_cell.draw()
                self._break_walls_r(next_i, next_j)