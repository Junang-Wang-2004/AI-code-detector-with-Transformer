v1 = int(input())
v2 = list(map(int, input().rstrip().split(' ')))
v3 = 1
for v4 in v2:
    if v4 % 2 == 1:
        v3 *= 3
    else:
        v3 *= 2
print(v3)
