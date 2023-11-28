from turtle import Turtle
from constants import SCREEN_HEIGHT

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, start_x: float, start_y: float) -> None:
        """ Creates a new paddle object, sets the color to white, and
            sets the starting position based on the start_x and start_y values."""
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self._move(start_x, start_y)

    def _move(self, x: float, y: float) -> None:
        self.goto(x, y)

    def move_up(self) -> None:
        """Moves the paddle up on the screen."""
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y <= ((SCREEN_HEIGHT / 2) - 60):
            self._move(self.xcor(), new_y)

    def move_down(self) -> None:
        """Moves the paddle down on the screen."""
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y >= ((SCREEN_HEIGHT / 2) - 60) * -1:
            self._move(self.xcor(), new_y)
