def f1(a1):
    v1 = [0 for v2 in range(n)]
    v3 = [0 for v2 in range(n)]
    v4 = 0
    v5 = -float('inf')
    for v6 in range(n):
        v4 += a1[v6][1]
        v1[v6] = max(v5, v4 - 2 * a1[v6][0])
        v5 = v1[v6]
    v4 = 0
    v5 = -float('inf')
    for v6 in sorted(range(n), reverse=True):
        v4 += a1[v6][1]
        v3[v6] = max(v5, v4 - (c - a1[v6][0]))
        v5 = v3[v6]
    v7 = max(v1[n - 1], v3[0])
    for v6 in range(n - 1):
        v7 = max(v7, v1[v6] + v3[v6 + 1])
    return v7
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    v3 = []
    for v4 in range(v1):
        v3.append(list(map(int, input().split())))
    v5 = sorted(v3, key=lambda x: x[0])
    v6 = 0
    v6 = max(v6, f1(v5))
    for v4 in range(v1):
        v5[v4][0] = v2 - v5[v4][0]
    v5 = sorted(v3, key=lambda x: x[0])
    v6 = max(v6, f1(v5))
    print(v6)
