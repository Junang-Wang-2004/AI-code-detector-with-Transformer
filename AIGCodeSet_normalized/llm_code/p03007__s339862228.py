v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = []
for v4 in range(len(v2) - 1):
    v3.append([v2.pop(0), v2.pop(len(v2) - 2)])
    v5 = v3[v4][0] - v3[v4][1]
    v2.insert(0, v5)
print(-v2[0])
v5 = v3[len(v3) - 1][1]
v3[len(v3) - 1][1] = v3[len(v3) - 1][0]
v3[len(v3) - 1][0] = v5
for v4 in range(len(v3)):
    print(v3[v4][0], v3[v4][1])
