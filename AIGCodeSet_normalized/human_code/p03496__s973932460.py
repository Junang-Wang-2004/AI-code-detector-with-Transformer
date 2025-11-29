v1 = int(input())
v2 = list(map(int, input().split()))
v3 = max(v2)
v4 = min(v2)
print(2 * v1 - 2)
if v3 + v4 >= 0:
    v5 = v2.index(v3)
    for v6 in range(v1):
        if v6 != v5:
            print(v5 + 1, v6 + 1)
    for v6 in range(v1 - 1):
        print(v6 + 1, v6 + 2)
else:
    v5 = v2.index(v4)
    for v6 in range(v1):
        if v6 != v5:
            print(v5 + 1, v6 + 1)
    for v6 in range(v1, 1, -1):
        print(v6, v6 - 1)
