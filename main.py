from core import (
    Node,
    bfs_level_order,
    count_change_iter,
    count_change_memo,
    count_change_naive,
    fib,
    fib_iter,
    inorder,
    postorder,
    preorder,
    quicksort,
    tree_height,
    tree_height_iter,
)


def main() -> None:
    values = [7, 3, 5, 3, -1, 8, 0]
    tree = Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))
    print("Лабораторна №4 — рекурсія та мемоізація, варіант 10")
    print("Quicksort:", quicksort(values))
    print("Preorder:", list(preorder(tree)))
    print("Inorder:", list(inorder(tree)))
    print("Postorder:", list(postorder(tree)))
    print("BFS:", bfs_level_order(tree))
    print("Висота:", tree_height(tree), tree_height_iter(tree))
    print("Fibonacci(30):", fib(30), fib_iter(30))
    print(
        "Розмін 12 (1,2,5):",
        count_change_naive(12, (1, 2, 5)),
        count_change_memo(12, (1, 2, 5)),
        count_change_iter(12, (1, 2, 5)),
    )


if __name__ == "__main__":
    main()
