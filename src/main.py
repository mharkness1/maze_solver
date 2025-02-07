from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    # Properties of the maze, cell size defined relative to the window size.
    num_rows = 12
    num_cols = 18
    margin_left = 50
    margin_top = 25
    screen_height = 800
    screen_width = 1000
    cell_size_x = (screen_width - (2*margin_left))/num_cols
    cell_size_y = (screen_height - (2*margin_top))/num_rows
    # Initialises the core window with the provided properties.
    win = Window(screen_width, screen_height)
    # Creates the maze, with the given gloval variables passed through including the window (which
    # contains the canvas).
    maze = Maze(margin_left, margin_top, num_rows, num_cols, cell_size_x, cell_size_y, win)
    # Takes the return value of the solve to output the value, by definition of the recursive maze
    # generation function, there should always be a solution.
    is_solvable = maze._solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        print("Maze solved")
    # Waits for the window close to pass through to the window manager protocol.
    win.wait_for_close()

if __name__ == "__main__":
    main()