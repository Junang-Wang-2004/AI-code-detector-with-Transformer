v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4, v5 in enumerate(v2):
    v6 = v4 + 1
    if v6 % 2 != 0 and v5 % 2 != 0:
        v3 += 1
print(v3)
