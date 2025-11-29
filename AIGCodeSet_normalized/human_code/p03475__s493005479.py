import sys
v1, *v2 = map(int, sys.stdin.read().split())
v2 = list(zip(*[iter(v2)] * 3))

def f1():
    for v1 in range(v1 - 1):
        v2 = 0
        for v3, v4, v5 in v2[v1:]:
            if v2 <= v4:
                v2 = v4 + v3
            else:
                v2 = v4 + (v2 - v4 + v5 - 1) // v5 * v5 + v3
        print(v2)
    print(0)
if __name__ == '__main__':
    f1()
