from elements.shape import Shape

class Tetris:
    def __init__(self, height, width):
        self.level = 2
        self.score = 0
        self.state = "play"
        self.zoom = 20
        self.x, self.y = 100, 60
        self.height, self.width = height, width
        self.grid = [[0] * width for _ in range(height)]
        self.shape = None

    def initialize_grid(self):
        # Initialize a grid corresponding to the width and height variables
        self.grid = [[0] * self.width for _ in range(self.height)]

    def new_shape(self):
        self.shape = Shape(3, 0)

    def block_intersects(self):
        # Iterate over all cells in the 4x4 matrix to check if cell is out of height/width bounds 
        # or if cell intersects with another block grid
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.block():
                    if (
                        i + self.shape.y > self.height - 1
                        or j + self.shape.x > self.width - 1
                        or j + self.shape.x < 0
                        or self.grid[i + self.shape.y][j + self.shape.x] > 0
                    ):
                        # Check grid area surrounding our block is not allocated to another block
                        return True
        return False

    def break_rows(self):
        rows = 0
        for i in range(1, self.height):
            zeros = self.grid[i].count(0)
            if zeros == 0:
                rows += 1
                for i1 in range(i, 1, -1):
                    self.grid[i1] = self.grid[i1 - 1].copy()
        self.score += rows ** 2

    def go_space(self):
        while not self.block_intersects():
            self.shape.y += 1
        self.shape.y -= 1
        self.place_block()

    def go_down(self):
        self.shape.y += 1
        if self.block_intersects():
            self.shape.y -= 1
            self.place_block()

    def place_block(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.block():
                    self.grid[i + self.shape.y][j + self.shape.x] = self.shape.color
        self.break_rows()
        self.new_shape()
        if self.block_intersects():
            self.state = "complete"

    def go_side(self, dx):
        prev_x = self.shape.x
        self.shape.x += dx
        if self.block_intersects():
            self.shape.x = prev_x

    def rotate(self):
        prev_r = self.shape.rotation
        self.shape.rotate()
        if self.block_intersects():
            self.shape.rotation = prev_r
