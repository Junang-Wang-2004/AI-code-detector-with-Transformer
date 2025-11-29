v1, v2 = map(int, input().split())
v3 = [int(input()) for v4 in range(v1)]
v3.sort()
v5 = []
for v4 in range(v2):
    if v4 + v2 - 1 > v1 - 1:
        break
    v5.append(v3[v4 + v2 - 1] - v3[v4])
print(min(v5))
