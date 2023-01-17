import sys
import string

n = len(sys.argv)


def filter_words(s: str, n: int) -> list:

    for c in string.punctuation:
        s = s.replace(c, ' ')

    for c in string.whitespace:
        s = s.replace(c, ' ')

    return [word for word in s.split() if len(word) > n]


if __name__ == "__main__":
    if n != 3 or not sys.argv[2].isnumeric():
        print("ERROR")
        exit(0)
    words = filter_words(sys.argv[1], int(sys.argv[2]))
    print(words)
