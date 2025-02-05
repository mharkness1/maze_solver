from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(50,50), Point(400,400))
    win.draw_line(line, "white")
    win.wait_for_close()

if __name__ == "__main__":
    main()