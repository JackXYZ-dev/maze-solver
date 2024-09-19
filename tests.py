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

    def test_break_walls_r_seed(self):
        maze = Maze(0, 0, 5, 5, 10, 10, seed=42)
        maze._break_walls_r(0, 0)

        # Check that all cells are visited
        for i in range(5):
            for j in range(5):
                self.assertTrue(maze._cells[i][j].visited)

        # Check that there's at least one broken wall for each cell (except edges)
        for i in range(5):
            for j in range(5):
                cell = maze._cells[i][j]
                broken_walls = sum([
                    not cell.has_top_wall,
                    not cell.has_bottom_wall,
                    not cell.has_left_wall,
                    not cell.has_right_wall
                ])
                if i == 0 or i == 4 or j == 0 or j == 4:
                    self.assertGreaterEqual(broken_walls, 1)
                else:
                    self.assertGreaterEqual(broken_walls, 2)

    def test_break_walls_r_invalid_start(self):
        maze = Maze(0, 0, 5, 5, 10, 10)
        with self.assertRaises(IndexError):
            maze._break_walls_r(5, 5)

    def test_break_walls_r_invalid_size(self):
        maze = Maze(0, 0, 5, 5, 10, 10)
        maze.num_rows = 10
        maze.num_cols = 10
        print(f"Maze dimensions: {maze.num_rows}x{maze.num_cols}")
        try:
            maze._break_walls_r(0, 0)
            print("_break_walls_r completed without raising an IndexError")
        except IndexError:
            print("IndexError was raised as expected")
        except Exception as e:
            print(f"Unexpected error occurred: {type(e).__name__}: {str(e)}")
        else:
            self.fail("IndexError not raised")

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 5, 5, 10, 10)
        maze._cells[0][0].visited = True
        maze._cells[1][1].visited = True
        maze._reset_cells_visited()
        for i in range(5):
            for j in range(5):
                cell = maze._cells[i][j]
                self.assertFalse(cell.visited)

    def test_reset_cells_visited_all_visited(self):
        maze = Maze(0, 0, 5, 5, 10, 10)
        for i in range(5):
            for j in range(5):
                maze._cells[i][j].visited = True
        maze._reset_cells_visited()
        for i in range(5):
            for j in range(5):
                cell = maze._cells[i][j]
                self.assertFalse(cell.visited)

    def test_reset_cells_visited_maze_size(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        for i in range(10):
            for j in range(10):
                maze._cells[i][j].visited = True
        maze._reset_cells_visited()
        for i in range(10):
            for j in range(10):
                cell = maze._cells[i][j]
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
