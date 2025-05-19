import pytest

from euler import Euler005


class TestEuler005:
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
