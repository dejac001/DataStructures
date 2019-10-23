class PyListSlow:
    """Dumb idea"""
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]


class PyListFast(PyListSlow):
    """Use default append method--implemented in C"""
    def __init__(self):
        PyListSlow.__init__(self)

    def append(self, item):
        self.items.append(item)


class PyList:
    def __init__(self, size=1):
        self.items = [None] * size
        self.numItems = 0

    def append(self, item):
        if self.numItems == len(self.items):
            # make list bigger by allocating a new list and copying
            # all the elements over to the new list
            newlst = [None] * self.numItems * 2
            for k in range(len(self.items)):
                newlst[k] = self.items[k]

            self.items = newlst

        self.items[self.numItems] = item
        self.numItems += 1


def main():
    p = PyList()

    for k in range(100):
        p.append(k)

    print(p.items)
    print(p.numItems)
    print(len(p.items))


if __name__ == '__main__':
    main()