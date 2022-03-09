from contextlib import contextmanager
from typing import Union

from pytest import mark, raises

from importer.size import assign_flip, CoinHolder, CoinToBig


@contextmanager
def does_not_raise():
    yield


class TestSize:
    @mark.parametrize(
        "test_coin_size, expected_coin_flip_size, exception",
        [
            (15.4, CoinHolder.J, does_not_raise()),
            (999, None, raises(CoinToBig)),
            (33.3, CoinHolder.D, does_not_raise()),
        ],
    )
    def test_assign_flip(
        self,
        test_coin_size: Union[float, int],
        expected_coin_flip_size: CoinHolder,
        exception,
    ) -> None:

        with exception:
            test = assign_flip(test_coin_size)
            assert test == expected_coin_flip_size
