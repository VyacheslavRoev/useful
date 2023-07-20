"""Сортировка слиянием."""

A = [44, 435, 9, 123, 54, 935, 1, -44, 84]


def duble_merge_sort(mass_1, mass_2):
    """Слияние двух списков."""
    result = []
    i, j = 0, 0

    while i < len(mass_1) and j < len(mass_2):
        if mass_1[i] <= mass_2[j]:
            result.append(mass_1[i])
            i += 1
        else:
            result.append(mass_2[j])
            j += 1

    if i < len(mass_1):
        result += mass_1[i:]
    if j < len(mass_2):
        result += mass_2[j:]

    return result


def merge_sort(A):
    """Функция сортировки."""
    if len(A) == 1:
        return A

    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    return duble_merge_sort(left, right)


print(*merge_sort(A))
