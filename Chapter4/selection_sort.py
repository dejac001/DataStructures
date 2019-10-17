def select(seq, start):
    """search from start to end of sequence"""
    minIndex = start

    for j in range(start + 1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j

    return minIndex


def selSort(seq):
    """sort a list using selection sort -> O(n^2)"""
    for i in range(len(seq)-1):  # dont need to sort last
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp