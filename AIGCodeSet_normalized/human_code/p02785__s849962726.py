v1, v2 = map(int, input().split())
v3 = sorted([int(i) for v4 in input().split()])
if v1 <= v2:
    print(0)
elif v2 == 0:
    print(sum(v3))
else:
    print(sum(v3[:-v2]))
