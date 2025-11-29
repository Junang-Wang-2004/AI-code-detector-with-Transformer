import sys

def f1():
    input = sys.stdin.buffer.readline
    v1, v2 = map(int, input().split())
    v3 = v1 // 2 // 2 + 1 if v1 % 2 == 0 else None
    v4 = 0
    v5, v6 = (0, v1 + 1)
    while v4 < v2:
        v5 += 1
        if v5 == v3:
            continue
        v6 -= 1
        print(v5, v6)
        v4 += 1
if __name__ == '__main__':
    f1()
