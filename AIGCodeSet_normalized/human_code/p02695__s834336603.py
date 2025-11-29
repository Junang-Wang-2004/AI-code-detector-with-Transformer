from itertools import combinations_with_replacement

def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = [[int(i) for v5 in input().split()] for v6 in range(v3)]
    v7 = 0
    for v8 in combinations_with_replacement(range(1, v2 + 1), v1):
        v9 = 0
        for v10, v11, v12, v13 in v4:
            v9 += v13 * (v8[v11 - 1] - v8[v10 - 1] == v12)
        v7 = max(v7, v9)
    print(v7)
if __name__ == '__main__':
    f1()
