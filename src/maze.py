import random
import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        # Needed because testing doesn't take a window, therefore no attribute to get.
        if win is not None:
            self.background_colour = win.background_colour
        else:
            self.background_colour = None

        if seed:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j, self.background_colour)

    def _draw_cell(self, i, j, background_colour=None):
        if self._win is None:
            return
        
        if background_colour is None:
            background_colour = self.background_colour
        
        x1 = self._x1 + (self._cell_size_x * i)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (self._cell_size_y * j)
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2, background_colour)
        self._animate()
                
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0, self.background_colour )
        self._cells[self._num_cols-1][self._num_rows-1].bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1, self.background_colour)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i - 1, j))

            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i + 1, j))
            
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j - 1))

            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            next_direction = random.randrange(len(to_visit))
            next_cell = to_visit[next_direction]

            #up
            if next_cell[1] == j-1:
                self._cells[i][j].top_wall = False
                self._cells[i][j-1].bottom_wall = False
            
            #down
            if next_cell[1] == j+1:
                self._cells[i][j].bottom_wall = False
                self._cells[i][j+1].top_wall = False
            
            #right
            if next_cell[0] == i+1:
                self._cells[i][j].right_wall = False
                self._cells[i+1][j].left_wall = False

            #left
            if next_cell[0] == i-1:
                self._cells[i][j].left_wall = False
                self._cells[i-1][j].right_wall = False
        
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_visited_cells(self):
        for col in self._cells:
         for cell in col:
                cell.visited = False

    def _solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        #left
        if i > 0 and not self._cells[i][j].left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        #right
        if i < self._num_cols - 1 and not self._cells[i][j].right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        #up
        if j > 0 and not self._cells[i][j].top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        #down
        if j < self._num_rows - 1 and not self._cells[i][j].bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False