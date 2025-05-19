import pytest

from euler import Euler001


class TestEuler001:
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
