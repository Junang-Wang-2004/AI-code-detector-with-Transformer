import sys
v1, v2 = map(int, sys.stdin.readline().split())
v3 = list(map(int, sys.stdin.readline().split()))
v4 = [list(map(int, sys.stdin.readline().split())) for v5 in range(v2)]
v3.sort(reverse=True)
v4.sort(key=lambda x: x[1], reverse=True)
for v6, v7 in v4:
    for v8 in range(min(v6, len(v3))):
        if v3[v8] < v7:
            v3[v8] = v7
        else:
            break
print(sum(v3))
