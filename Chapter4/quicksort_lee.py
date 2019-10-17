import random


def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start + 1
    j = stop - 1

    while i <= j:
        while i <= j and not pivot < seq[i]:  # need < for sort (calls __lt__ method)
            i += 1
        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            # switch
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i += 1
            j -= 1

    seq[pivotIndex] = seq[j]
    seq[j] = pivot

    return j


def quicksortRecursively(seq, start, stop):
    if start >= stop - 1:
        return

    pivotIndex = partition(seq, start, stop)

    quicksortRecursively(seq, start, pivotIndex)
    quicksortRecursively(seq, pivotIndex+1, stop)


def quicksort(seq):
    # randomize the sequence first
    for i in range(len(seq)):
        j = random.randint(0, len(seq)-1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp

    quicksortRecursively(seq, 0, len(seq))
    return seq


def main():
    print(quicksort(list((5,8,2,6,8,1,0,7))))


if __name__ == '__main__':
    main()