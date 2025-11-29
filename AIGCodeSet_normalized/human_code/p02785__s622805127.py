v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = v1 - v2
if v4 < 0:
    v5 = 0
else:
    v6 = sorted(v3)[:v4]
    v5 = sum(v6)
print(v5)
