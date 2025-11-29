v1 = int(input())
v1 = 3 ** v1
v2 = list(map(int, input().split()))
v2 = [2 if i % 2 == 0 else 1 for v3 in v2]
v4 = 1
for v3 in v2:
    v4 *= v3
print(v1 - v4)
