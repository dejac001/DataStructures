from sorting_algorithms import lists_to_test


class MyTimer:
    def time(self):
        from timeit import timeit
        with open('timing.csv', 'w') as f:
            f.write('%20s,%20s,%20s,%20s\n' % ('"Selection Sort"', '"Merge Sort"', '"Quick Sort"', '"Tree Sort"'))
            for l in lists_to_test:
                length = len(eval(l))
                f.write('%20f,' % timeit('sort(%s)' % l,
                                          setup='from sorting_algorithms.selection_sort import sort'))
                f.write('%20f,' % timeit('sort(%s, 0, %i)' % (l, length),
                                         setup='from sorting_algorithms.merge_sort import sort'))
                f.write('%20f,' % timeit('sort(%s, 0, %i)' % (l, length-1),
                                          setup='from sorting_algorithms.quick_sort import sort'))
                f.write('%20f\n' % timeit('sort(%s)' % l,
                                        setup='from sorting_algorithms.tree_sort import sort'))


if __name__ == '__main__':
    MyTimer().time()
