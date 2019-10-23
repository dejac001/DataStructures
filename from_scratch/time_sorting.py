from from_scratch import lists_to_test


class MyTimer:
    def time(self):
        from timeit import timeit
        with open('timing.txt', 'w') as f:
            f.write('%20s,%20s\n' % ('"Selection Sort"', '"Merge Sort"'))
            for l in lists_to_test:
                length = len(eval(l))
                f.write('%20f,' % timeit('sort(%s)' % l,
                                          setup='from from_scratch.selection_sort import sort'))
                f.write('%20f\n' % timeit('sort(%s, 0, %i)' % (l, length),
                                         setup='from from_scratch.merge_sort import sort'))


if __name__ == '__main__':
    MyTimer().time()
