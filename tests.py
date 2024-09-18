import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        x1, y1 = 0, 0
        num_rows, num_cols = 5, 5
        cell_size_x, cell_size_y = 10, 10

        maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y)

        self.assertFalse(maze._cells[0][0].has_top_wall, "The entrance wall wasn't removed")
        self.assertFalse(maze._cells[num_cols-1][num_rows-1].has_bottom_wall, "The exit wall wasn't removed")

if __name__ == "__main__":
    unittest.main()
