v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 0
for v4 in range(v1 // 2):
    if v2[v4] == v2[v1 // 2 + v4]:
        v3 += 1
    else:
        break
print(v3)
