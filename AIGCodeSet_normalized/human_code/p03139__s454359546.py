v1, v2, v3 = list(map(int, input().split()))
if v2 + v3 <= v1:
    print(min(v2, v3), 0)
else:
    print(min(v2, v3), v2 + v3 - v1)
