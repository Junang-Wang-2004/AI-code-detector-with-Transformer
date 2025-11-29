v1, v2 = map(int, input().split())
if v1 < 10:
    v2 += 100 * (10 - v1)
print(v2)
