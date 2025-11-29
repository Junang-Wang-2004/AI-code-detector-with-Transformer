v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sorted(v2, reverse=True)
v4 = 0
v5 = v1 // 2
for v6 in range(v5):
    v4 = v4 + v3[v6] * 2
v4 = v4 - v3[0]
if v1 % 2 == 1:
    v4 = v4 + v3[(v1 - 1) // 2]
print(v4)
