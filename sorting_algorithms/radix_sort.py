"""sort words alphabetically"""


class Queue:
    """First in, first out"""
    def __init__(self):
        self.items = []

    def add(self, item):
        """add to queue"""
        self.items.append(item)

    def remove(self):
        """remove from queue"""
        return self.items.pop(0)

    def __iter__(self):
        return self.items.__iter__()

    def __len__(self):
        return self.items.__len__()


class Stack(Queue):
    """Last in, first out"""
    def __init__(self):
        Queue.__init__(self)

    def remove(self):
        return self.items.pop(-1)


def sort(my_list: list):

    my_stack = Stack()
    my_stack.items = my_list

    # find largest string length
    largest_length = -1
    for i in my_stack:
        if len(i) > largest_length:
            largest_length = len(i)

    # i = largest_length - 1  # index for comparison; start at end

    # make stacks
    sum = ''
    for i in my_stack:
        sum += i
    unique_letters_sorted = sorted(set(sum))
    data = {
        i: Stack() for i in unique_letters_sorted
    }
    data[None] = Stack()  # for those with length less than i

    def termination_func(lst, length):
        count = 0
        for i in lst:
            if len(i) <= length:
                count += 1
        return count > 1

    # termination condition: when there is 1 or less word of length i + 1
    while termination_func(my_stack, largest_length):

        # take from queue (my_list) to stacks
        while len(my_stack) > 0:
            i = my_stack.remove()
            if len(i) < largest_length:
                data[None].add(i)
            else:
                data[i[largest_length-1]].add(i)

        # tack back from stacks to queue
        for i in range(len(data[None])):
            my_stack.add(data[None].remove())
        for key in unique_letters_sorted:
            for i in range(len(data[key])):
                my_stack.add(data[key].remove())

        largest_length -= 1

    return my_stack.items


if __name__ == '__main__':
    a = sort(['i', 'is', 'it', 'its'])
    print(a)
