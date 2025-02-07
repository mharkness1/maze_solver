from tkinter import Tk, BOTH, Canvas

class Window:
    # Initialises the Tkinter window as the root, and the canvas as the main widget.
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        # Built in protocol that accesses the native window manager to close.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # Accesses the canvas background colour which here is the default system background.
        self.background_colour = self.__canvas['background']
    # Method redraw calls two update functions.
    def redraw(self):
        # Update_idletasks = Skips te first action and upadtes only things in the idle queue.
        self.__root.update_idletasks()
        # Update = runs any events in the queue that is due; then runs all idle events in queue (including 
        # those added to the queue after update() was called (but not suring the given loop).
        self.__root.update()
    # Wait for close continually calls the two update functions whilst the window is open.
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    # Close alters the state, it is passed into the window manager protocol, and stops the update loop
    def close(self):
        self.__running = False
    # Draw line on window. Which is the only item drawn. Sets the default colour to white. Drawn to canvas.
    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)
# Defines the coordinate system - it is independent of the canvas and window, but fundamentally
# operates on the canvas.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Lines takes two points i.e., 4 coordinates to define.
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    # Draw operates on teh canvas to create a line between two points.
    def draw(self, canvas, fill_color="white"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

