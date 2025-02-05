from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    #TO DO Generate some cells to test the implementation.
    cell1 = Cell(win)
    cell1.left_wall = False
    cell1.draw(100,100,125,125)

    cell2 = Cell(win)
    cell2.top_wall = False
    cell2.draw(320,450,345,475)

    cell1.draw_move(cell2)

    #line = Line(Point(50,50), Point(400,400))
    #win.draw_line(line, "white")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()