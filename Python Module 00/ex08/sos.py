import sys

morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
}


def to_morse(s: str):
    i = 0
    length = len(s)
    for c in s:
        if c not in morse:
            print("ERROR")
            exit(0)
    for c in s:
        print(morse[c], end='')
        i += 1
        if i < length:
            print(end=' ')


n = len(sys.argv)

if __name__ == "__main__":
    for i in range(1, n):
        s = sys.argv[i].lower()
        to_morse(s)
        if i != n - 1:
            print(' / ', end='')
        else:
            print()
