import bisect
v1 = int(input())
v2 = sorted([int(input()) for v3 in range(v1)])
v4 = [v2[0]]
for v3 in range(len(v2)):
    if v2[v3] >= v4[-1]:
        v4.append(v2[v3])
    else:
        v4[bisect.bisect_left(v4, v2[v3])] = v2[v3]
print(len(v4))
