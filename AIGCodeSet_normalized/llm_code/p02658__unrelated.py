v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in range(v1):
    v3 *= v2[v4]
    if v3 > 10 ** 18:
        v3 = -1
        break
print(v3)
