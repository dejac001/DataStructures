class PyList:
    def __init__(self, contents=[], size=10):
        """Contents allows for initial construction.
        Useful if programmer knows he/she is going to add a specific number of items right away to the list.
        """
        self.items = [None]*size
        self.numItems = 0
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if 0 <= index < self.numItems:
            return self.items[index]
        raise IndexError('PyList index out of range')

    def __setitem__(self, key, value):
        if 0 <= key < self.numItems:
            self.items[key] = value
            return
        raise IndexError('PyList assignment index out of range')

    def __add__(self, other):
        result = PyList(size=self.numItems + other.numItems)

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(self.numItems, self.numItems + other.numItems):
            result.append(other.items[i])

        return result

    def __makeroom(self):
        """increase list size by 1/4 to make more room"""
        newlen = (self.size // 4) + self.size + 1
        newlst = [None]*newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.size = newlen

    def append(self, item):
        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems] = item
        self.numItems += 1

    def insert(self, i, e):
        if self.numItems == self.size:
            self.__makeroom()

        if i < self.numItems:
            # no choice but to copy each element after point where
            #   we want to insert the new value to the next location in the list
            #   But, works best if we start from the right end of the list and work our way back
            for j in range(self.numItems-1, i-1, -1):
                self.items[j+1] = self.items[j]

            self.items[i] = e
            self.numItems += 1
        else:
            # if index provided is larger than the size of the list, the new item, e, is appended to the end of the list
            self.append(e)

    def __delitem__(self, key):
        for i in range(key, self.numItems-1):
            self.items[i] = self.items[i+1]
        self.numItems -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False
        return True

    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

    def __len__(self):
        return self.numItems

    def __contains__(self, item):
        """Linear search [O(n) complexity]"""
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        return False

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + repr(self.items[i])
            if i < self.numItems - 1:
                s = s + ', '
        s = s + ']'
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + repr(self.items[i])
            if i < self.numItems - 1:
                s = s + ', '
        s = s + '])'
        return s


def main():
    sampleList = PyList(['a', 'b', 'c'])


if __name__ == '__main__':
    main()
