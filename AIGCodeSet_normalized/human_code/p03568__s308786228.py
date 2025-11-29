v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in v2:
    if v4 % 2 == 0:
        v3 += 1
print(3 ** v1 - 2 ** v3)
