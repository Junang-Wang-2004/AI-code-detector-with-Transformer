v1 = int(input())
v2 = list(map(int, input().split()))
print(2 * v1 - 1)
if abs(max(v2)) >= abs(min(v2)):
    v3 = v2.index(max(v2))
    for v4 in range(v1):
        print(v3 + 1, v4 + 1)
    for v5 in range(v1 - 1):
        print(v5 + 1, v5 + 2)
else:
    v3 = v2.index(min(v2))
    for v4 in range(v1):
        print(v3 + 1, v4 + 1)
    for v5 in range(v1 - 1, 0, -1):
        print(v5 + 1, v5)
