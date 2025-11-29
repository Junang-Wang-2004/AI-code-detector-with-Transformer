v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = [i + j for v5, v6 in v2]
v4.sort(reverse=True)
v7 = sum(v4[::2]) - sum([v6 for v5, v6 in v2])
print(v7)
