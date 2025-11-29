v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v3.insert(v2[v4] - 1, v4 + 1)
if v3 == list(range(1, v1 + 1)):
    for v5 in v3:
        print(v5)
else:
    print(-1)
