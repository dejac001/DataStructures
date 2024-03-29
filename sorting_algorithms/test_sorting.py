import unittest
from sorting_algorithms import lists_to_test


class MyTestCase(unittest.TestCase):
    def test_lists_for_testing(self):
        for lst in map(eval, lists_to_test):
            for i in lst:
                self.assertEqual(type(i), type(int()))

    def test_merge(self):
        from sorting_algorithms.merge_sort import merge
        _lst = [0, 2, 3, 1, 3, 6]
        merge(_lst, 0, 3, 6)
        self.assertEqual(_lst, sorted(_lst))

    def test_selection_sort(self):
        from sorting_algorithms.selection_sort import sort
        for lst in map(eval,lists_to_test):
            sort(lst)
            self.assertEqual(lst, sorted(lst))

    def test_merge_sort(self):
        from sorting_algorithms.merge_sort import sort
        for lst in map(eval,lists_to_test):
            sort(lst, 0, len(lst))
            self.assertEqual(lst, sorted(lst))

    def test_quick_sort(self):
        from sorting_algorithms.quick_sort import sort
        for lst in map(eval, lists_to_test):
            sort(lst, 0, len(lst)-1)
            self.assertEqual(lst, sorted(lst))

    def test_tree_sort(self):
        from sorting_algorithms.tree_sort import sort
        for lst in map(eval, lists_to_test):
            self.assertEqual(sort(lst), sorted(lst))


if __name__ == '__main__':
    unittest.main()
