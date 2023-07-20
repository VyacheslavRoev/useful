"""Быстрая сортировка."""
from random import randint


A = [23, 5, 90, -231, -4, 12, 99, 7]


def quick_sort(A):
    if len(A) <= 1:
        return A

    x = A[randint(0, len(A) - 1)]
    left = [i for i in A if i < x]
    mid = [i for i in A if i == x]
    right = [i for i in A if i > x]

    return quick_sort(left) + mid + quick_sort(right)


print(quick_sort(A))
