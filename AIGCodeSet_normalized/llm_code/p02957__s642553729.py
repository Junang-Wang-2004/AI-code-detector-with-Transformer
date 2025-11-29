v1, v2 = map(int, input().split())
if (v1 + v2) % 2 == 0:
    v3 = (v1 + v2) // 2
else:
    v3 = (v1 + v2) // 2 + 1
print(v3)
