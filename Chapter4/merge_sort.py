"""Divides list until left with lists of size 1.
Two sorted sublists can be merged into one sorted list in O(n) time.
A list can be divided into lists of size 1 by repeatedly splitting in O(log n)time,
resulting in a complexity of O(n log n) for merge sort.

One criticism of the merge sort algorithm is that the elements of the two
sublists cannot be merged without copying to a new list and then back again.


Since there are log n levels to the merge sort algorithm and each level
takes O(n) to merge, the algorithm is O(n log n)
"""


def merge(seq, start, mid, stop):
    """Merge two sublists

    :param seq: list
    :type seq: list
    :param start: index starting first list
    :type start: int
    :param mid: index stopping first list & starting second list
    :type mid: int
    :param stop: index stopping second list
    :type stop: int
    :return: merged list, lst
    :rtype: list
    """
    lst = []
    i = start
    j = mid

    # merge the two lists while each has more elements. Stops when one or other sublist is empty
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1

    # Copy in the rest of start to mid sequence
    while i < mid:
        lst.append(seq[i])
        i += 1

    # copy the elements back to orig seq
    for i in range(len(lst)):
        seq[start + i] = lst[i]


def mergeSortRecursively(seq, start, stop):
    """

    :param seq: list
    :param start: start index
    :param stop: stop index
    :return:
    """
    if start >= stop-1:
        # base case, we have sorted into sublist sizes of 1
        return

    mid = (start + stop)//2     # middle index (int)
    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)


def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))
