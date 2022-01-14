import pytest

from euler import Euler001, Euler002, Euler003, Euler004, Euler005


class TestEuler1_10:
    @pytest.mark.parametrize(
        "input,expected",
        [
            (1000, 233168),
            (49, 543),
            (8456, 16687353),
            (19564, 89301183),
        ],
    )
    def test_Euler001(self, input, expected):
        assert Euler001(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (8, 10),
            (10, 10),
            (34, 44),
            (60, 44),
            (1000, 798),
            (100000, 60696),
            (4000000, 4613732),
        ],
    )
    def test_Euler002(self, input, expected):
        assert Euler002(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (2, 2),
            (3, 3),
            (5, 5),
            (7, 7),
            (8, 2),
            (13195, 29),
            (600851475143, 6857),
        ],
    )
    def test_Euler003(self, input, expected):
        assert Euler003(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (2, 9009),
            (3, 906609),
        ],
    )
    def test_Euler004(self, input, expected):
        assert Euler004(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (5, 60),
            (7, 420),
            (10, 2520),
            (13, 360360),
            (20, 232792560),
        ],
    )
    def test_Euler005(self, input, expected):
        assert Euler005(input) == expected
