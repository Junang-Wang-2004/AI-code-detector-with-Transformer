v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [a for v4 in v2 if v4 > 0]
v5 = [v4 for v4 in v2 if v4 <= 0]
v3.sort()
v5.sort(reverse=True)
if len(v5) == 0:
    print(sum(v3) - 2 * v3[0])
    v6 = v3[0]
    for v7 in range(1, len(v3) - 1):
        print(str(v6) + ' ' + str(v3[v7]))
        v6 -= v3[v7]
    print(str(v3[-1]) + ' ' + str(v6))
elif len(v3) == 0:
    print(-1 * sum(v5) + 2 * v5[0])
    v6 = v5[0]
    for v7 in range(1, len(v5)):
        print(str(v6) + ' ' + str(v5[v7]))
        v6 -= v5[v7]
else:
    print(sum(v3) - sum(v5))
    v6 = v5[0]
    for v7 in range(len(v3) - 1):
        print(str(v6) + ' ' + str(v3[v7]))
        v6 -= v3[v7]
    if len(v3) > 0:
        print(str(v3[-1]) + ' ' + str(v6))
        v6 = v3[-1] - v6
    for v7 in range(1, len(v5)):
        print(str(v6) + ' ' + str(v5[v7]))
        v6 -= v5[v7]
