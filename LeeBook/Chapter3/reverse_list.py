def revList(lst):
    # base case
    if len(lst) == 0:
        return []

    restrev = revList(lst[1:])  # everytime you call, gets smaller
    first = lst[0:1]
    return restrev + first


def revList2(lst):

    def revListHelper(index):
        if index == -1:
            return list()
        restrev = revListHelper(index-1)
        first = [lst[index]]

        return first + restrev
    return revListHelper(len(lst)-1)


def main():
    print(revList([1,2,3,4]))
    print(revList2([1,2,3,4]))


if __name__ == '__main__':
    main()