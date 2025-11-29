import sys
input = sys.stdin.readline

def f1():
    v1 = int(input())
    v2 = [list(map(int, input().split())) for v3 in range(v1)]
    v4 = int(100000.0)
    v5 = v4
    v6 = []
    v7 = [True] * (v5 + 1)
    for v3 in range(2, v5 + 1):
        if v7[v3]:
            v6.append(v3)
            for v8 in range(2 * v3, v5 + 1, v3):
                v7[v8] = False
    v9 = [0] * (v4 + 1)
    for v10 in v6:
        if v10 & 1:
            v11 = (v10 + 1) // 2
            if v7[v11]:
                v9[v10] = 1
    for v3 in range(1, v4 + 1):
        v9[v3] += v9[v3 - 1]
    for v3 in range(v1):
        v12, v13 = v2[v3]
        print(v9[v13] - v9[v12 - 1])
if __name__ == '__main__':
    f1()
