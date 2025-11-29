import sys
input = sys.stdin.readline

def f1():
    v1 = int(input())
    v2 = [0] * v1
    for v3 in range(v1):
        v2[v3] = int(input())
    v4 = 0
    v5 = -1
    for v3, v6 in enumerate(v2):
        if v6 > v3 or v6 > v5 + 1:
            v4 = -1
            break
        if v6 > 0:
            v4 += 1
            if v5 + 1 != v6:
                v4 += v6 - 1
        v5 = v6
    print(v4)
if __name__ == '__main__':
    f1()
