import bisect
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [v2[0]]
for v5 in v2[1:]:
    if v5 > v4[-1]:
        v4.append(v5)
    else:
        v4[bisect.bisect_left(v4, v5)] = v5
print(v1 - len(v4) + 1)
