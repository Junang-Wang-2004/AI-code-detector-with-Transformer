import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = []
v5 = 0
for v6 in range(v2 + 1):
    for v7 in range(v2 - v6 + 1):
        if v6 + v7 > v1:
            break
        v4.append(v3[:v6] + v3[v1 - v7:])
for v8 in v4:
    for v9 in range(v2 - len(v8)):
        if v8 == []:
            break
        elif min(v8) < 0:
            v8.pop(v8.index(min(v8)))
        elif min(v8) > 0:
            break
        if v8 != []:
            v10 = sum(v8)
            if v10 > 0 and v10 > v5:
                v5 = v10
print(v5)
