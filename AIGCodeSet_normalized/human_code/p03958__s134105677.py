import sys
v1, v2, *v3 = map(int, open(0).read().split())
v3.sort(reverse=True)
v4 = min(v3[0], sum(v3[1:]) + 1) + sum(v3[1:])
print(v1 - min(v1, v4))
