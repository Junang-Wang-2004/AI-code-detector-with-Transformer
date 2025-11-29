v1 = int(input())
v2 = sorted(map(int, input().split()))
v2.reverse()
v3 = [sum(v2)] * v1
v4 = 1
for v5 in range(1, v1):
    v3[v5] = v3[v5 - 1] - v2[v5 - 1]
    if v3[v5] * 2 < v2[v5 - 1]:
        break
    else:
        v4 += 1
print(v4)
