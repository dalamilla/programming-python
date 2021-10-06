class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
      return  f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = ""

    if self.width  > 50 or self.height > 50:
      return "Too big for picture."

    for _ in range(self.height):
      picture += f'{"":*^{self.width}}\n'
    return picture

  def get_amount_inside(self, figure):
    return int(self.get_area() / figure.get_area())


class Square(Rectangle):

  def __init__(self, side):
      self.side = side
      super().__init__(side, side)

  def __str__(self):
      return  f'Square(side={self.side})'

  def set_side(self, side):
    self.height = side
    self.width = side
    self.side = side

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)
