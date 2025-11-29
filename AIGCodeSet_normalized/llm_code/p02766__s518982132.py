v1, v2 = map(int, input().split())
v3 = 0
while v1 > 0:
    v1 //= v2
    v3 += 1
print(v3)
