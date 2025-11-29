v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
while v4 <= v2:
    v4 = v4 + v3[v5]
    v5 = v5 + 1
print(v5)
