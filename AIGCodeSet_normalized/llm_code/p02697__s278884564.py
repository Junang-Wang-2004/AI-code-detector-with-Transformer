v1, v2 = map(int, input().split())
if v1 % 2 == 0:
    for v3 in range(v2):
        print(v3 + 1, v1 - v3)
else:
    for v3 in range(v2):
        print(v3 + 1, v1 - v3 - 1)
