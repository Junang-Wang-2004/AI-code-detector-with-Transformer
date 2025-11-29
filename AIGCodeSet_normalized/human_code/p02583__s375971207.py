import itertools
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in itertools.combinations(v2, 3):
    v4 = list(v4)
    v4.sort()
    if v4[0] != v4[1] and v4[1] != v4[2]:
        if v4[2] < v4[0] + v4[1]:
            v3 += 1
print(v3)
