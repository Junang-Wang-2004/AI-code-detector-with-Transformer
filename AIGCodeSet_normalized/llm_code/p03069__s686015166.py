v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4, v5 in zip(v2, v2[1:]):
    if v4 + v5 == '#.':
        v3 += 1
print(v3)
