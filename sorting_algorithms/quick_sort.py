def get_pivot_val(my_list: list, i_start: int, i_end: int):
    """get pivot value

    .. note:
        here, j is included in the list

    :return: median of start, end, and mean index
    """
    i_mid = (i_start + i_end) // 2
    val_start, val_mid, val_end = my_list[i_start], my_list[i_mid], my_list[i_end]

    if val_start < val_end:
        # val_start < val_end
        if val_mid < val_start:
            # val_mid < val_start < val_end
            return val_start
        else:
            # val_start <= val_mid < val_end
            return val_mid
    else:
        # val_end <= val_start
        if val_mid < val_end:
            # val_mid < val_end <= val_start
            return val_end

        # val_end <= val_mid <= val_end
        return val_mid


def sort(my_list: list, i_start: int, i_end: int):
    """quick sort in-place"""
    if i_start >= i_end:
        # list of length 1 is already sorted
        # i can be > j if list is len(3) and pivot is beginning
        return

    i, j = i_start, i_end

    val_pivot = get_pivot_val(my_list, i_start, i_end)

    while i < j:
        if my_list[i] > val_pivot:
            if my_list[j] < val_pivot:
                # change in place, add and subtract
                my_list[i], my_list[j] = my_list[j], my_list[i]
                i += 1
                j -= 1
            elif my_list[j] == val_pivot:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                j -= 1
        elif my_list[i] == val_pivot and my_list[j] < val_pivot:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
        if my_list[i] < val_pivot:
            i += 1
        if my_list[j] >= val_pivot:
            j -= 1

    # new pivot here is marked by i == j
    sort(my_list, i_start, i - 1)
    sort(my_list, j+1, i_end)


if __name__ == '__main__':
    l = [5, 8, 2, 6, 9, 1, 0, 7]
    sort(l, 0, len(l)-1)
    print(l)

    l = [-1, -10, 0, 44, 2]
    sort(l, 0, len(l)-1)
    print(l)

    l = [-1, -10, 0, 0, 44, 2]
    sort(l, 0, len(l)-1)
    print(l)

    l = [1, 7, 9, 3, 4, -1, -10, 0, 44, 2, 0, 3, 2, 0, 11, 12, 18, 2, -7, 11, 55]
    sort(l, 0, len(l)-1)
    print(l)
