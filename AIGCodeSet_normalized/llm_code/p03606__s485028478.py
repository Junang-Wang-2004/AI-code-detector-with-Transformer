v1 = int(input())
sum = 0
v2 = [False for v3 in range(100000)]
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    for v6 in range(v4 - 1, v5):
        v2[v6] = True
print(sum(v2))
