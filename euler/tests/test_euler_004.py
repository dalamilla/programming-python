import pytest

from euler import Euler004


class TestEuler004:
    @pytest.mark.parametrize(
        "input,expected",
        [
            (2, 9009),
            (3, 906609),
        ],
    )
    def test_Euler004(self, input, expected):
        assert Euler004(input) == expected
