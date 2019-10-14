def revString(s):
    if len(s) == 0:
        return ""

    restrev = revString(s[1:])
    first = s[0:1]
    return restrev + first


def main():
    print(revString('hello'))


if __name__ == '__main__':
    main()