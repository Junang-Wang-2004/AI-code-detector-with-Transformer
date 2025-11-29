v1, v2 = map(int, input().split())
if v1 % 2 == 1:
    for v3 in range(1, v2 + 1):
        print(v3, v1 - v3 + 1)
else:
    for v3 in range(1, v2 + 1):
        print(v3, v1 - v3 + (v3 <= v1 // 4))
