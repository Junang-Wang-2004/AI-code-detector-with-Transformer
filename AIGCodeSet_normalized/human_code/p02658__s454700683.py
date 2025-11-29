v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 1
v4 = 10 ** 18
for v5 in v2:
    if v5 == 0:
        v3 = 0
        break
v5 = v1 - 1
while v5 >= 0:
    if v2[v5] == 0:
        v3 = 0
        break
    if v3 > v4 / v2[v5]:
        v3 = v4 + 1
        break
    v3 *= v2[v5]
    if v2[v5] > v4:
        break
    v5 -= 1
if v3 > v4:
    v3 = -1
print(v3)
