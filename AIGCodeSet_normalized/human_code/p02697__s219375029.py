v1, v2 = map(int, input().split())
if v2 % 2 == 1:
    for v3 in range(v2 // 2):
        print(v3 + 1, v2 - v3)
    for v3 in range(v2 // 2 + 1):
        print(v2 + v3 + 1, 2 * v2 + 1 - v3)
else:
    for v3 in range(v2 // 2):
        print(v3 + 1, v2 + 1 - v3)
    for v3 in range(v2 // 2):
        print(v2 + v3 + 2, 2 * v2 + 1 - v3)
