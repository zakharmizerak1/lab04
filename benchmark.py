from timeit import repeat

from core import count_change_iter, count_change_memo, count_change_naive


def main() -> None:
    amount, coins = 30, (1, 2, 5, 10)
    methods = (count_change_naive, count_change_memo, count_change_iter)
    print(f"Розмін {amount} монетами {coins}")
    for method in methods:
        result = method(amount, coins)
        duration = min(repeat(lambda: method(amount, coins), number=3, repeat=3)) / 3
        print(f"{method.__name__}: {result} способів, {duration:.6f} с")


if __name__ == "__main__":
    main()
