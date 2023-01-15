import sys

n = len(sys.argv)

for i in range(n - 1, 0, -1):
    print(sys.argv[i][::-1].swapcase(), end = (' ' if i > 1 else '\n'))
