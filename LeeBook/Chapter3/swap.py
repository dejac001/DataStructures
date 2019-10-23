"""Swap every two elements of the original string"""


def swap(string: str):
    if len(string) <= 1:
        return string
    return string[1] + string[0] + swap(string[2:])


def main():
    print(swap('ahahahah'))
    print(swap('0132430'))


if __name__ == '__main__':
    main()
