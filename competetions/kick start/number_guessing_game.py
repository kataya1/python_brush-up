import sys


def guesser():
    A, B = [int(s) for s in input().split(" ")]
    N = int(input())
    starter, ender = (A + 1), B

    for i in range(N):
        k = (ender + starter) // 2
        sys.stdout.write("%d\n" % (k))
        sys.stdout.flush()
        s = input()
        if (s == "CORRECT"):
            break
        elif (s == "TOO_SMALL"):
            starter = k + 1
        elif (s == "TOO_BIG"):
            ender = k - 1
        else:
            exit()


def processor():
    t = int(input())
    for i in range(t):
        guesser()


processor()
