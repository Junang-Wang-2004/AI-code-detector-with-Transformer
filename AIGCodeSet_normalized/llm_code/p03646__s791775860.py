v1 = int(input())
v2 = 2
while v1 > 0:
    v2 += 1
    v1 -= v2 - 1
print(v2)
print(1, end=' ')
for v3 in range(v2 - 2):
    print(0, end=' ')
print(1)
