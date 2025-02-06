from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.left_wall = True
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visisted = False
    
    def draw(self, x1, y1, x2, y2, background_colour):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.background_colour = background_colour
        
        if self.left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line, self.background_colour)

        if self.top_wall:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line, self.background_colour)

        if self.right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line, self.background_colour)

        if self.bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line, self.background_colour)
    
    def draw_move(self, to_cell, undo=False):
        self._center_x = (self._x1 + self._x2)/2
        self._center_y = (self._y1 + self._y2)/2
        self.undo = undo

        to_cell._center_x = (to_cell._x1 + to_cell._x2)/2
        to_cell._center_y = (to_cell._y1 + to_cell._y2)/2

        line = Line(Point(self._center_x, self._center_y), Point(to_cell._center_x, to_cell._center_y))
        if self.undo == False:
            self._win.draw_line(line, "red")
        elif self.undo == True:
            self.win.draw_line(line, "gray")