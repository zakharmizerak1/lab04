import pytest

from core import count_change_iter, count_change_memo, count_change_naive


@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (0, (1, 2), 1),
        (4, (1, 2), 3),
        (5, (1, 2, 5), 4),
        (11, (1, 2, 5), 11),
        (3, (2, 4), 0),
        (10, (), 0),
        (0, (), 1),
        (10, (5, 1, 5, 2), 10),
    ],
)
def test_change(amount: int, coins: tuple[int, ...], expected: int) -> None:
    assert count_change_naive(amount, coins) == expected
    assert count_change_memo(amount, coins) == expected
    assert count_change_iter(amount, coins) == expected


@pytest.mark.parametrize("amount, coins", [(-1, (1, 2)), (3, (0, 1)), (3, (-1, 1))])
def test_change_invalid(amount: int, coins: tuple[int, ...]) -> None:
    for method in (count_change_naive, count_change_memo, count_change_iter):
        with pytest.raises(ValueError):
            method(amount, coins)


def test_coins_not_mutated() -> None:
    coins = [5, 1, 2]
    count_change_memo(8, coins)
    assert coins == [5, 1, 2]
