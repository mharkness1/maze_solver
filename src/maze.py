import random
import time
from cell import Cell
# Defines the maze class, one instance is called during each run.
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        # Defines the top left point of the maze i.e., x and y. Passed in during main()
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
        # if a given seed is passed in, then the random function is given that seed (which makes it
        # deterministic)
        if seed:
            random.seed(seed)
        # Defines an empty list to contain the cells and their attributes to iterate through.
        self._cells = []
        # Calls the active methods of a maze. Create cells - populates the list with a list of lists.
        self._create_cells()
        # Removes the top wall of the top left cell and removes the bottom wall of the bottom right cell.
        self._break_entrance_and_exit()
        # Calls break wall function (which initialises the maze) from the lists of lists of cells.
        # 0,0 makes the recusive function start at the top left.
        self._break_walls_r(0, 0)
        # When breaking walls, visisted member of cell class is updated to true. The resset function sets the
        # visited attribute to false for all cells (as this attribute is then reused for solving)
        self._reset_visited_cells()
    # Create cells fn initialises the list of lists that holds the cell properties. i is num cols, the fn
    # creates i number of empty lists. j is the num of rows, for each i a list of length j cell objects is created.
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            # The list of cells representing the row is then appended to the outer list.
            self._cells.append(col_cells)
        # for every cells in the _cells, calls the draw cell function which takes indexes and converts to coordinates
        # and then calls the draw method on each cell. WIth background colour for faux deletion.
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j, self.background_colour)
    # Primative draw cell function, takes indexes and background_colour for 'deletion'.
    def _draw_cell(self, i, j, background_colour=None):
        # When tests are called no window is generated. This the _draw_cell function doesn't need to be called.
        if self._win is None:
            return
        # Ensures that background colour is set. Even if the window isn't called/opened.
        if background_colour is None:
            background_colour = self.background_colour
        # Generates the coordinates from the top left coords of the maze and the relevant indexes. i represents cols i.e., x axis.
        x1 = self._x1 + (self._cell_size_x * i)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (self._cell_size_y * j)
        y2 = y1 + self._cell_size_y
        # Having generated the coordinates calls the .draw cell function. And animtes, which adds a delay after each
        # action in the queue, giving the appearance of animation due to the delay.
        self._cells[i][j].draw(x1, y1, x2, y2, background_colour)
        self._animate()
    # Animate function (doesn't activate during testing). Otherwise calls redraw method of the window (which re-runs the two update
    # functions) and adter a delay.
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.001)
    # Breaks the top wall of the top left cell and the bottom wall of the bottom right cell.
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0, self.background_colour )
        self._cells[self._num_cols-1][self._num_rows-1].bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1, self.background_colour)
    # Recursively breaks walls in order to generate the actual maze based on the index.
    def _break_walls_r(self, i, j):
        # Updates the cell property so the same cell isn't visited repeatedly.
        self._cells[i][j].visited = True
        # Creates infinite loop (break condition is every cell has been visited)
        while True:
            # Empty list created to keep track of 'options'.
            to_visit = []
            # Left -- if the col number is greater than zero, means there is a cell to the right. Check it hasn't been visited.
            if i > 0 and not self._cells[i-1][j].visited:
                # If exists add it to the to_visit list.
                to_visit.append((i - 1, j))
            # Right -- similar logic, but this time checks that the col is not the last column, as otherwise there is no cell to the right.
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i + 1, j))
            # Top -- same logic as above.
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j - 1))
            # Bottom -- same logic as above.
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j + 1))
            # If all adjacent cells have already been visited, i.e., weren't added to the to_visit list, it draws the cell and returns.
            # By this point with all adjacent cells visited it will have had the status of the walls updated.
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            # Next direction choses a random number corresponding to the neighbouring unvisited cells.
            # Next cell takes the index of the randomly selected cell from the to_visit list.
            next_direction = random.randrange(len(to_visit))
            next_cell = to_visit[next_direction]

            # Top -- if the next cell chosen is above. This gets rid of the current cells top wall, and the cell being visited next's
            # bottom wall i.e., connecting the two cells.
            if next_cell[1] == j-1:
                self._cells[i][j].top_wall = False
                self._cells[i][j-1].bottom_wall = False
            
            # Bottom -- the same logic as above.
            if next_cell[1] == j+1:
                self._cells[i][j].bottom_wall = False
                self._cells[i][j+1].top_wall = False
            
            # Right -- the same logic as above.
            if next_cell[0] == i+1:
                self._cells[i][j].right_wall = False
                self._cells[i+1][j].left_wall = False

            # Left -- the same logic as above.
            if next_cell[0] == i-1:
                self._cells[i][j].left_wall = False
                self._cells[i-1][j].right_wall = False
            # Calls the function again starting with the selected next cell, meaning every cell will have two walls broken
            # Once when it is designated the next_cell and again when it is the current cell and choosing a direct to visit.
            self._break_walls_r(next_cell[0], next_cell[1])
            # The recursion unwinds when it hits a cell that has had all its neighbours visited. It unwinds to until to_visit was last not empty
            # and then proceeds again i.e., it generates with a depth first recusive formula.
    # This function resets the visited value for all cells so it can be reused in the solving function.
    def _reset_visited_cells(self):
        for col in self._cells:
         for cell in col:
                cell.visited = False
    # Calls and returns the recursive solving function initialised to start at the top left corner.
    def _solve(self):
        return self._solve_r(0, 0)
    # Recursive solving algorith DFS algorithm. Begins with animate, which calls the update functions and waits during every execution.
    def _solve_r(self, i, j):
        self._animate()
        # Sets the current cell to visited.
        self._cells[i][j].visited = True
        # Ends the loop when the bottom right square is visited.
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # Left -- if not in the leftmost col, and it doesn't have a leftwall i.e., Not Not (will execute), also checks it hasn't been visited before.
        if i > 0 and not self._cells[i][j].left_wall and not self._cells[i-1][j].visited:
            # Draws the move from the current cells to the çell to the left.
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            # Calls the recursion algorith again, this always starts by going left. And so on, until the recursive fn return true.
            # Then the instance returns true as it means the bottom right cell must have been visited in the recursive path.
            if self._solve_r(i - 1, j):
                return True
            # if the recusion never returns true, it means that it hit a dead end and therefore re-draws the whole path as red i.e., undo = True.
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # Right - same logic as above.
        if i < self._num_cols - 1 and not self._cells[i][j].right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # Top - same logic as above.
        if j > 0 and not self._cells[i][j].top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # Bottom - same logic as above.
        if j < self._num_rows - 1 and not self._cells[i][j].bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        # If all the avove conditions fail, it has nowhere else to visit and check, therefore it returns false as it is at a dead end.
        return False