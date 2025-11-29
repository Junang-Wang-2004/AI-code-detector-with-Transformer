def f1(a1):
    v1 = len(a1)
    v2 = [[0] * v1 for v3 in range(v1)]
    for v4 in range(v1):
        for v5 in range(v4 + 1, v1):
            v2[v4][v5] = max(v2[v4][v5 - 1], v2[v4 + 1][v5])
    return v2[0][v1 - 1]

def f2():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    print(f1(v2))
if __name__ == '__main__':
    f2()
