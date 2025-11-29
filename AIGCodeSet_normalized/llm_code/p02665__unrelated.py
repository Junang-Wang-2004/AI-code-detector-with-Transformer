def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    if v2[v1] == 0:
        return -1
    v3 = 1
    for v4 in range(v1):
        if v2[v4] == 0:
            return -1
        v3 += v2[v4]
        v2[v4 + 1] -= 2 * v2[v4]
    return v3
print(f1())
