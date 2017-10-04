"""
Here are defined the constants of the language.
You will alos find shortcuts for repetitive values in the code like UP and DOWN.
"""

from .vector import Pos

# Defining directions
UP = Pos(0, -1)
DOWN = Pos(0, 1)
LEFT = Pos(-1, 0)
RIGHT = Pos(1, 0)

DIRECTIONS = (UP, RIGHT, DOWN, LEFT)

LEFT_TILT = 0
RIGHT_TILT = 1
