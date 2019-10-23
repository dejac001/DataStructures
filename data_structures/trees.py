class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        if not self.left is None:
            for i in self.left:
                yield i

        yield self.val

        if not self.right is None:
            for j in self.right:
                yield j


class BinaryTree(BinaryNode):
    def __init__(self, initial_value):
        BinaryNode.__init__(self, initial_value)

    def add_value(self, val):
        if val < self.val:
            if self.left is None:
                self.left = BinaryNode(val)
            else:
                BinaryTree.add_value(self.left, val)
        else:
            if self.right is None:
                self.right = BinaryNode(val)
            else:
                BinaryTree.add_value(self.right, val)

    def __iter__(self):
        for i in self.left:
            yield i

        yield self.val

        for j in self.right:
            yield j

    def sort(self):
        return self.__iter__()


def textbook_example():
    """Lee, p. 172"""
    tree = BinaryTree(5)
    for val in [5, 8, 2, 1, 4, 6, 7]:
        tree.add_value(val)

    print(list(tree))

    print(tree.sort())

if __name__ == '__main__':
    textbook_example()
