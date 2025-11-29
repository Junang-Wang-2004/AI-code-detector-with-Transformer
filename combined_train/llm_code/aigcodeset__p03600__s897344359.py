v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]

def f1():
    for v1 in range(v1):
        for v2 in range(v1):
            for v3 in range(v1):
                v4 = v2[v2][v1] + v2[v1][v3]
                if v4 < v2[v2][v3]:
                    return -1
    v5 = 10 ** 18
    v6 = 0
    for v2 in range(v1):
        for v3 in range(v2 + 1, v1):
            for v1 in range(v1):
                if v1 == v2 or v1 == v3:
                    continue
                v4 = v2[v2][v1] + v2[v1][v3]
                if v4 == v2[v2][v3]:
                    v6 += v2[v2][v3]
                    v2[v2][v3] = v5
                    v2[v3][v2] = v5
                    break
    return v6
print(sum((sum(a) for v4 in v2)) // 2 - f1())
