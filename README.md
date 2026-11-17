# Лабораторна робота №4 — варіант 10

**Рекурсія та мемоізація; індивідуальний варіант №10**

Студент: Мізерак Захар Володимирович, ФЕП-21.

## Запуск (Windows)

```powershell
python -m pip install -r requirements.txt
python main.py
python -m pytest -v
python -m mypy .
python -m black --check .
python -m ruff check .
```

Код предметної логіки відділено від демонстраційного запуску.

## Реалізація
Реалізовано quicksort, три рекурсивні обходи дерева, ітеративні BFS/DFS, Fibonacci з lru_cache та ітеративний аналог, рекурсивну й ітеративну висоту, гібридний quicksort.

## Індивідуальне завдання: розмін монет
Реалізовано `count_change_naive`, `count_change_memo` (через `lru_cache`) та `count_change_iter`; кількість комбінацій без урахування порядку монет. Для вимірювання виконайте `python benchmark.py`. Час залежить від комп’ютера.
