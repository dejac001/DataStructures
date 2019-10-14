def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()
    if seq == emptySeq:
        return emptySeq

    return reverse(seq[1:]) + seq[0:1]


def main():
    print(reverse([1,2,3,4]))
    print(reverse('hello'))


if __name__ == '__main__':
    main()