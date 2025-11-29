v1, v2, v3 = map(int, input().split())
min = max(0, v2 + v3 - v1)
max = min(v2, v3)
print(str(max) + ' ' + str(min))
