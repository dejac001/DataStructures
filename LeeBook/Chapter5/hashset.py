

class HashSet:

    def __init__(self, contents=[]):
        self.items = [None]*10
        self.numItems = 0

        for item in contents:
            self.add(item)

    class __Placeholder:
        """For deleting items. If we need to delete an item in the
            middle of the chain, we cant replace w/ None b/c this would cut the chain of values.
            Instead, use Placeholder object."""

        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __add(self, item, items):
        """Takes care of adding an item to the HashSet list
        and is a helper function for th actual add method.

        Finding a None indicates end of linear chain and end of linear searching.
        If item is not in list, then the item is added either at the location
        of the first __placeholder object or at the location
        of the None value at the end of the chain

        To insure that we get an amortized complexity of O(1),
        the list must never be full or almost full.

        """
        idx = hash(item) % len(items)
        loc = -1

        # exit when find a None
        while items[idx] is not None:
            if items[idx] == item:
                # item already in set
                return False

            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)  # idx can become 0 here

        if loc < 0:
            loc = idx

        items[loc] = item
        return True

    def __rehash(oldList, newList):
        """Load factor is too high so must make new list & rehash."""
        for x in oldList:
            if x is not None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)

        return newList

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                # Here, we choose to double the size of the list when rehashing
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items))

    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] is not None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] is None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)

        return False

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] is not None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] is not None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] is not None:
            if self.items[idx] == item:
                return self.items[idx]

            idx = (idx + 1) % len(self.items)

        return None
