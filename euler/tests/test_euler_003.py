import pytest

from euler import Euler003


class TestEuler003:
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
