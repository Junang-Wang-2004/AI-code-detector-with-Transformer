v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6, v7 = map(int, input().split())
    v3.append([abs(v5), abs(v6), abs(v7)])
v3.sort(key=lambda x: sum(x), reverse=True)
print(sum([sum(x) for v8 in v3[:v2]]))
