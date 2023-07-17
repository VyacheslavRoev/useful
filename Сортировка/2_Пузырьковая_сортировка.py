"""Пузырьковая сортировка."""

A = [45, 3, 34, 95, 43, 4, 54, 999, 234, 23, 53]


def bubble_sort(A):
    """Алгоритм сортировки."""
    s = True
    while s:
        s = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                s = True
    return A


print(bubble_sort(A))
