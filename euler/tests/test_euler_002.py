import pytest

from euler import Euler002


class TestEuler002:
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
