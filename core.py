from __future__ import annotations

from collections import deque
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True, slots=True)
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None


def quicksort(xs: Sequence[int]) -> list[int]:
    if len(xs) <= 1:
        return list(xs)
    pivot = xs[len(xs) // 2]
    return (
        quicksort([x for x in xs if x < pivot])
        + [x for x in xs if x == pivot]
        + quicksort([x for x in xs if x > pivot])
    )


def preorder(node: Node | None) -> Iterator[int]:
    if node is not None:
        yield node.key
        yield from preorder(node.left)
        yield from preorder(node.right)


def inorder(node: Node | None) -> Iterator[int]:
    if node is not None:
        yield from inorder(node.left)
        yield node.key
        yield from inorder(node.right)


def postorder(node: Node | None) -> Iterator[int]:
    if node is not None:
        yield from postorder(node.left)
        yield from postorder(node.right)
        yield node.key


def bfs_level_order(node: Node | None) -> list[int]:
    if node is None:
        return []
    queue = deque([node])
    result: list[int] = []
    while queue:
        current = queue.popleft()
        result.append(current.key)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return result


def dfs_preorder_iter(node: Node | None) -> list[int]:
    if node is None:
        return []
    stack = [node]
    result: list[int] = []
    while stack:
        current = stack.pop()
        result.append(current.key)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def tree_height(node: Node | None) -> int:
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_height_iter(node: Node | None) -> int:
    if node is None:
        return 0
    queue = deque([(node, 1)])
    height = 0
    while queue:
        current, depth = queue.popleft()
        height = max(height, depth)
        if current.left is not None:
            queue.append((current.left, depth + 1))
        if current.right is not None:
            queue.append((current.right, depth + 1))
    return height


def quicksort_hybrid(xs: Sequence[int]) -> list[int]:
    if len(xs) < 32:
        result = list(xs)
        for i in range(1, len(result)):
            current = result[i]
            j = i - 1
            while j >= 0 and result[j] > current:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = current
        return result
    pivot = xs[len(xs) // 2]
    return (
        quicksort_hybrid([x for x in xs if x < pivot])
        + [x for x in xs if x == pivot]
        + quicksort_hybrid([x for x in xs if x > pivot])
    )


def normalize_coins(coins: Sequence[int]) -> tuple[int, ...]:
    if any(coin <= 0 for coin in coins):
        raise ValueError("Coin denominations must be positive")
    return tuple(sorted(set(coins)))


def count_change_naive(amount: int, coins: Sequence[int]) -> int:
    if amount < 0:
        raise ValueError("Amount must be nonnegative")
    values = normalize_coins(coins)

    def solve(remaining: int, index: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0 or index == len(values):
            return 0
        return solve(remaining - values[index], index) + solve(remaining, index + 1)

    return solve(amount, 0)


def count_change_memo(amount: int, coins: Sequence[int]) -> int:
    if amount < 0:
        raise ValueError("Amount must be nonnegative")
    values = normalize_coins(coins)

    @lru_cache(maxsize=None)
    def solve(remaining: int, index: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0 or index == len(values):
            return 0
        return solve(remaining - values[index], index) + solve(remaining, index + 1)

    return solve(amount, 0)


def count_change_iter(amount: int, coins: Sequence[int]) -> int:
    if amount < 0:
        raise ValueError("Amount must be nonnegative")
    values = normalize_coins(coins)
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in values:
        for current in range(coin, amount + 1):
            ways[current] += ways[current - coin]
    return ways[amount]
