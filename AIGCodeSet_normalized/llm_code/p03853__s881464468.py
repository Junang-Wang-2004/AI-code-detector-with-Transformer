v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(input())
for v4 in range(2 * v1):
    print(v3[v4 // 2])
