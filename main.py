from window import *


def main():
    win = Window(800, 600)
    test_point = Point(10, 10)
    test_point2 = Point(500, 500)
    test_line = Line(test_point, test_point2)
    win.draw_line(test_line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
