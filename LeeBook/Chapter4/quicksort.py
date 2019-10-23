def get_pivot(A, low, hi):
    """Get median value of three index options"""
    mid = (hi + low) // 2   # middle index
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot


def partition(A, low, hi):
    """

    :param A: list to be partitioned
    :param low: low index
    :param hi: high index
    :return: border
    """
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]  # swap pivot value into left-most index of value
    border = low

    for i in range(low, hi + 1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return (border)


def quick_sort2(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort2(A, low, p-1)
        quick_sort2(A, p+1, high)


def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)
    return A


if __name__ == '__main__':
    print(quick_sort([17, 41, 5, 22, 54, 6, 29, 3, 13]))
