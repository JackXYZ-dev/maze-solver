from window import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)
    test_cell = Cell(True, True, True, True, 300, 500, 300, 500, win)
    test_cell2 = Cell(True, True, False, True, 120, 150, 100, 200, win)
    test_cell.draw()
    test_cell2.draw()
    test_cell.draw_move(test_cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()
