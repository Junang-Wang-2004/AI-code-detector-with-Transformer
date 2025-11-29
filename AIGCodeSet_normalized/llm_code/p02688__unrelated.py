v1, v2 = map(int, input().split())
v3 = set(range(1, v1 + 1))
for v4 in range(v2):
    v5 = int(input())
    v3 -= set(map(int, input().split()))
print(len(v3))
