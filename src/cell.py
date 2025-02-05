class Cell:
    def __init__(self, win):
        self.left_wall = True
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        pass