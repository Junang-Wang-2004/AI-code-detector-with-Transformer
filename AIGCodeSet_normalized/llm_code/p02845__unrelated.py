def f1(a1, a2):
    v1 = [0] * (a1 + 1)
    v1[0] = 1
    for v2 in range(1, a1 + 1):
        v1[v2] = (v1[v2 - 1] + v1[max(0, v2 - a2[v2 - 1] - 1)]) % 1000000007
    return v1[a1]
v1 = int(input())
v2 = list(map(int, input().split()))
print(f1(v1, v2))
