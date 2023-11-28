from turtle import Turtle

INITIAL_MOVE_SPEED = 0.1

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self._x_move = 10
        self._y_move = 10
        self._move_speed = INITIAL_MOVE_SPEED

    def move(self) -> None:
        """Moves the ball along the x and y axes."""
        new_x = self.xcor() + self._x_move
        new_y = self.ycor() + self._y_move
        self.goto(new_x, new_y)

    def get_move_speed(self) -> float:
        """Returns the ball's current move speed."""
        return self._move_speed

    def bounce_y(self) -> None:
        """Reverses the ball direction on the y-axis."""
        self._y_move *= -1

    def bounce_x(self) -> None:
        """Reverses the ball direction on the x-axis and increases the ball speed."""
        self._x_move *= -1
        self._move_speed *= 0.9

    def reset_position(self) -> None:
        """ Resets the ball's position to the center of the screen, and resets the ball's speed."""
        self._move_speed = INITIAL_MOVE_SPEED
        self.goto(0, 0)
