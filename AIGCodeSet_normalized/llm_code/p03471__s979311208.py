import sys

def f1():
    v1, v2 = map(int, sys.stdin.readline().split())
    for v3 in range(v2 // 10000):
        for v4 in range((v2 - 10000 * v3) // 5000):
            v5 = v1 - v3 - v4
            if 10000 * v3 + 5000 * v4 + 1000 * v5 == v2:
                print(v3, v4, v5)
                return
    print('-1 -1 -1')
if __name__ == '__main__':
    f1()
