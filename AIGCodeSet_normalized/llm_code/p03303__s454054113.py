v1 = input()
v2 = int(input())
v3 = 1
v4 = v3 * v2
while v4 <= len(v1) - 3:
    v5 = v1[0]
    v1 = v1[3:]
    v5 += v1[0]
    v3 += 1
    v4 = v3 * v2
print(v5)
