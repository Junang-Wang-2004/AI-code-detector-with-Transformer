v1 = int(input())
v2 = 100
v3 = 0
while v2 < v1:
    v2 = v2 + int(v2 * 0.01)
    v3 += 1
print(v3)
