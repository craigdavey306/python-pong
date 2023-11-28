from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        """Creates a scoreboard object."""
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self._left_score = 0
        self._right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.clear()
        self.goto(-100, 200)
        self.write(self._left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self._right_score, align='center', font=('Courier', 80, 'normal'))

    def left_point(self):
        """Increments the left player's point."""
        self._left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Increments the right player's point."""
        self._right_score += 1
        self.update_scoreboard()
