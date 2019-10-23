def sort(my_list: list):
    """Selection sort in-place"""
    for i in range(len(my_list)):
        i_min, val_min = i, my_list[i]
        for j in range(i+1, len(my_list)):
            if my_list[j] < val_min:
                i_min, val_min = j, my_list[j]
        # switch i and i_min
        my_list[i], my_list[i_min] = my_list[i_min], my_list[i]


from sorting_algorithms import lists_to_test


def time():
    import timeit
    times = []
    for l in lists_to_test:
        times.append(
            timeit.timeit('sort(%s)' % l, setup='from __main__ import sort')
        )
    return times


def test():
    for l in map(eval,lists_to_test):
        sort(l)
        assert l == sorted(l), 'Incorrect sorting'


def main():
    test()
    times = time()
    print(times)


if __name__ == '__main__':
    main()
