def merge(l1: list, i, istop, jstop):
    """Merge two *sorted* lists.
       - jstop is *not* part of the second list
       - istop is *not* part of the first list
    """
    start = i
    j = istop
    newlist = []
    while i < istop:
        if j == jstop or l1[i] < l1[j]:
            newlist.append(l1[i])
            i += 1
        elif j < jstop:
            newlist.append(l1[j])
            j += 1

    # copy back to original sequence
    for ii in range(len(newlist)):
        l1[start + ii] = newlist[ii]


def sort(my_list: list, i_start: int, i_end: int):
    """Merge sort in-place"""
    if i_start >= i_end - 1:
        # if i == j - 1, length of list is 1 (first list has len 1 and other list has len 0)
        #   need > b/c when call w/ i_mid+1 below, dont check if larger than j
        # thus, below, we will only be sorting two lists, each of length 1
        return

    i_mid = (i_end + i_start)//2
    sort(my_list, i_start, i_mid)
    sort(my_list, i_mid, i_end)
    merge(my_list, i_start, i_mid, i_end)
