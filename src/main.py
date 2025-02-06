from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    num_rows = 9
    num_cols = 12
    margin_left = 50
    margin_top = 25
    screen_height = 800
    screen_width = 1000
    cell_size_x = (screen_width - (2*margin_left))/num_cols
    cell_size_y = (screen_height - (2*margin_top))/num_rows

    win = Window(screen_width, screen_height)
    maze = Maze(margin_left, margin_top, num_rows, num_cols, cell_size_x, cell_size_y, win)
    is_solvable = maze._solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        print("Maze solved")

    win.wait_for_close()

if __name__ == "__main__":
    main()