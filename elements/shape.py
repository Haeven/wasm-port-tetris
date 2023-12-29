import random
from lib.enums import colors

class Shape:
  # These equate to our Tetris blocks
  # each outer array represents the block,
  # while the inner arrays represent the rotations
  # where each digit corresponds to a position on a 4x4 matrix
  shapes = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
  ]

  # Instantiate the class with random type and color
  # Set default rotation, this value will index the shapes array
  # to determine appropriate rotation coordinates
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.type = random.randint(0, len(self.shapes) - 1)
    self.color = random.randint(1, len(colors) - 1)
    self.rotation = 0

  def block(self):
    return self.shapes[self.type][self.rotation]

  def rotate(self):
    # Quick way to compute index of next rotation by dividing the current rotation
    # value by the length of the possible rotations, giving the index of the
    # desired next rotation, resetting back to 0 by rounding down division 
    # once end of rotations array is reached (rotation or {max-len - 1} / max-len == 0.xx == 0)
    self.rotation = (self.rotation + 1) % len(self.shapes[self.type])
