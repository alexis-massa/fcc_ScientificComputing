import copy
import random


class Hat:

    def __init__(self, **kwargs):
        if len(kwargs) < 1:
            raise ValueError("There should be at least one ball in the Hat")
        self.contents = [
            color for color, amount in kwargs.items() for _ in range(amount)
        ]

    def draw(self, N: int) -> list[str]:
        """
        Draw `n` balls from the hat. Drawn balls are removed from the hat.

        Args:
            N (int): The number of draws

        Returns:
            list[str]: The balls drawn
        """
        if N >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        return [
            self.contents.pop(random.randrange(len(self.contents)))
            for _ in range(N)
        ]


def experiment(
    hat: "Hat",
    expected_balls: dict[str, int],
    num_balls_drawn: int,
    num_experiments: int,
) -> float:
    """
    Perform `num_experiments` experiments of drawing `num_balls_drawn` balls 
    and return the probability of drawing `expected_balls`.

    Args:
        hat (Hat): The hat to pull from
        expected_balls (dict[str, int]): The expected balls drawn
        num_balls_drawn (int): The amount of balls drawn
        num_experiments (int): The number of experiments

    Returns:
        float: The probability of drawing `expected_balls` in `num_balls_drawn` draws from the `hat` across `num_experiments` experiments
    """
    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success += all(drawn_balls.count(color) >= amount for color, amount in expected_balls.items())

    return success / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
print(probability)
