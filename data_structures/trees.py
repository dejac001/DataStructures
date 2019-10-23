class BinaryNode:
    def __init__(self, val, left=None, right=None, count=1):
        self.root = None
        self.val = val
        self.count = count
        self.left = left
        self.right = right

    def __iter__(self):
        if not self.left is None:
            for i in self.left:
                yield i

        for k in range(self.count):
            yield self.val

        if not self.right is None:
            for j in self.right:
                yield j


class BinaryTree(BinaryNode):
    def __init__(self, val):
        BinaryNode.__init__(self, val)
        self.root = val

    def add_value(self, val):
        if val < self.val:
            if self.left is None:
                self.left = BinaryNode(val)
            else:
                BinaryTree.add_value(self.left, val)
        elif val == self.val:
            self.count += 1
        elif val > self.val:
            if self.right is None:
                self.right = BinaryNode(val)
            else:
                BinaryTree.add_value(self.right, val)

    def __iter__(self):
        for i in self.left:
            yield i

        for k in range(self.count):
            yield self.val

        for j in self.right:
            yield j

    def sort(self):
        return self.__iter__()

    def __repr__(self):
        val_rep = '%i(%i)' % (self.val, self.count)
        if self.val == self.root:
            val_rep = '*' + val_rep + '*'
        if self.left is not None:
            if self.right is None:
                return val_rep
            else:
                # both are not none:
                return '%s << %s >> %s' % (
                    BinaryTree.__repr__(self.left), val_rep, BinaryTree.__repr__(self.right)
                )
        elif self.right is not None:
            # left is None but right isnt
            return '%s >> %s' % (val_rep, BinaryTree.__repr__(self.right))
        else:
            # they are both none
            return val_rep


def textbook_example():
    """Lee, p. 172"""
    tree = BinaryTree(5)
    for val in [5, 8, 2, 1, 4, 6, 7]:
        tree.add_value(val)

    print(list(tree))

    print(tree.sort())


def test():
    from sorting_algorithms import lists_to_test
    for l in map(eval, lists_to_test):
        tree = BinaryTree(l[0])
        for i in l[1:]:
            tree.add_value(i)
        print(tree)



if __name__ == '__main__':
    # textbook_example()

    test()