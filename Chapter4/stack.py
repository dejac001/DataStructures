class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError('Attempt to pop an empty stack')

        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.isEmpty():
            raise RuntimeError('Attempt to get top of empty stack')

        topIdx = len(self.items) - 1
        return self.items[topIdx]

    def isEmpty(self):
        return len(self.items) == 0


class Stack2:
    """Implement Stack but with node data type"""
    pass


def main():
    s = Stack()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        s.push(k)

    assert s.top() == 9, 'Test 1 failed'
    print('test1 passed')

    while not s.isEmpty():
        lst2.append(s.pop())

    lst2.reverse()

    assert lst2 == lst, 'Test 2 failed'
    print('test2 passed')

    try:
        s.pop()
        print('Test 3 failed')
    except RuntimeError:
        print("test 3 passed")
    except:
        print('test 3 failed')

    try:
        s.top()
        print('test 4 failed')
    except RuntimeError:
        print('test 4 passed')
    except:
        print('test 4 failed')


if __name__ == '__main__':
    main()