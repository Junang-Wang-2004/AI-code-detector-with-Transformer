v1 = int(input())
v2 = input()
v3 = 0
for v4 in range(v1 - 1):
    if v2[v4] == v2[v4 + 1]:
        v3 += 1
print(v3)
