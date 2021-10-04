import unittest

from euler_001 import Euler001 
from euler_002 import Euler002 
from euler_003 import Euler003
from euler_004 import Euler004
from euler_005 import Euler005

class TestEuler1_10(unittest.TestCase):

  def test_Euler001(self):
      
    tests = [
        (1000, 233168),
        (49, 543),
        (8456, 16687353),
        (19564, 89301183),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler001(value), expected)


  def test_Euler002(self):

    tests = [
      (8, 10),
      (10, 10),
      (34, 44),
      (60, 44),
      (1000, 798),
      (100000, 60696),
      (4000000, 4613732),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler002(value), expected)

  def test_Euler003(self):

    tests = [
      (2, 2),
      (3, 3),
      (5, 5),
      (7, 7),
      (8, 2),
      (13195, 29),
      (600851475143, 6857),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler003(value), expected)

  def test_Euler004(self):

    tests = [
      (2, 9009),
      (3, 906609),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler004(value), expected)

  def test_Euler005(self):

    tests = [
      (5, 60),
      (7, 420),
      (10,2520),
      (13,360360),
      (20,232792560),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler005(value), expected)

if __name__ == '__main__':
    unittest.main()
