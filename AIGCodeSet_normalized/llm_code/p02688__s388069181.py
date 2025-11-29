v1, v2 = map(int, input().split())
v3 = [0] * (v1 + 1)
v4 = 0
for v5 in range(v2):
    v6 = int(input())
    v7 = list(map(int, input().split()))
    for v8 in range(v6):
        v3[v7[v8]] += 1
for v5 in range(1, v1 + 1):
    if v3[v5] == 0:
        v4 = v4 + 1
print(v4)
