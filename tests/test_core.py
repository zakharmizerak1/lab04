from random import Random

import pytest

from core import (
    Node,
    bfs_level_order,
    dfs_preorder_iter,
    fib,
    fib_iter,
    inorder,
    postorder,
    preorder,
    quicksort,
    quicksort_hybrid,
    tree_height,
    tree_height_iter,
)


def tree() -> Node:
    return Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))


@pytest.mark.parametrize("items", [[], [1], [3, 2, 1], [2, 2, 1, 3, 2], [-3, 0, -3, 9]])
def test_sort(items: list[int]) -> None:
    original = items[:]
    assert quicksort(items) == sorted(items)
    assert quicksort_hybrid(items) == sorted(items)
    assert items == original


def test_random_sort() -> None:
    items = [Random(42).randint(-100, 100) for _ in range(100)]
    assert quicksort(items) == sorted(items)


def test_tree() -> None:
    t = tree()
    assert list(preorder(t)) == [4, 2, 1, 3, 6, 7]
    assert list(inorder(t)) == [1, 2, 3, 4, 6, 7]
    assert list(postorder(t)) == [1, 3, 2, 7, 6, 4]
    assert bfs_level_order(t) == [4, 2, 6, 1, 3, 7]
    assert dfs_preorder_iter(t) == list(preorder(t))


def test_empty_tree() -> None:
    assert list(preorder(None)) == []
    assert list(inorder(None)) == []
    assert list(postorder(None)) == []
    assert bfs_level_order(None) == []
    assert dfs_preorder_iter(None) == []
    assert tree_height(None) == tree_height_iter(None) == 0


def test_heights() -> None:
    assert tree_height(tree()) == tree_height_iter(tree()) == 3


def test_fibonacci() -> None:
    assert [fib(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert all(fib(n) == fib_iter(n) for n in range(70))
    assert fib.cache_info().hits > 0
    fib.cache_clear()
    assert fib(20) == 6765


@pytest.mark.parametrize("function", [fib, fib_iter])
def test_negative_fibonacci(function: object) -> None:
    with pytest.raises(ValueError):
        if function is fib:
            fib(-1)
        else:
            fib_iter(-1)
