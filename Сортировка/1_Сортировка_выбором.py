"""Сортировка выбором."""

A = [45, 3, 34, 95, 43, 4, 54, 999, 234, 23, 53]


def select_sort(A):
    """Алгоритм сортировки."""
    for i in range(len(A) - 1):
        min_index = i
        for k in range(i + 1, len(A)):
            if A[k] < A[min_index]:
                min_index = k
        A[i], A[min_index] = A[min_index], A[i]
    return A


print(select_sort(A))
