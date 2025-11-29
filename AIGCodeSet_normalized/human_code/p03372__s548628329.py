from itertools import accumulate
import sys
input = sys.stdin.readline

def f1():
    v1, v2 = map(int, input().split())
    v3, v4 = ([0], [0])
    for v5 in range(v1):
        v6, v7 = map(int, input().split())
        v3.append(v6)
        v4.append(v7)
    v8 = [0]
    v9 = [0]
    for v10 in range(v1, 0, -1):
        v8.append(v2 - v3[v10])
        v9.append(v4[v10])
    v4, v9 = (list(accumulate(v4)), list(accumulate(v9)))
    v11, v12 = ([v9[0] - v8[0]], [v9[0] - 2 * v8[0]])
    for v10 in range(1, v1 + 1):
        v13 = v9[v10] - v8[v10]
        v14 = v9[v10] - 2 * v8[v10]
        v11.append(max(v11[v10 - 1], v13))
        v12.append(max(v12[v10 - 1], v14))
    v15 = max(v4[v1] - v3[v1] + v12[0], v4[v1] - 2 * v3[v1] + v11[0])
    for v10 in range(1, v1 + 1):
        v15 = max(v15, v4[v1 - v10] - v3[v1 - v10] + v12[v10], v4[v1 - v10] - 2 * v3[v1 - v10] + v11[v10])
    print(v15)
if __name__ == '__main__':
    f1()
