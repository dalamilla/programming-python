import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for i, k in kwargs.items():
      self.contents += [i] * k

  def draw(self, number_balls):
    select_balls = []
    if number_balls > len(self.contents):
      return self.contents
    for x in range(number_balls):
      select_balls += [self.contents.pop(random.randrange(len(self.contents)))]
    return select_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count_sucess = 0

  for _ in range(num_experiments):
    experiment = copy.deepcopy(hat)
    balls = experiment.draw(num_balls_drawn)
    balls_dict = {}

    for ball in balls:
      if ball in balls_dict:
        balls_dict[ball] += 1
      else:
        balls_dict[ball] = 1

    count_greater_equal = 0
    for key in expected_balls:
      if key in balls_dict:
        if balls_dict[key] >= expected_balls[key]:
          count_greater_equal += 1

    if count_greater_equal == len(expected_balls):
      count_sucess += 1

  return  count_sucess / num_experiments
