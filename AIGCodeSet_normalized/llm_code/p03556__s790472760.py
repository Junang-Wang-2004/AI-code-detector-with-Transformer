v1 = int(input())
for v2 in range(v1, 1, -1):
    v3 = int(pow(v2, 0.5))
    if v3 * v3 == v2:
        break
print(v3)
