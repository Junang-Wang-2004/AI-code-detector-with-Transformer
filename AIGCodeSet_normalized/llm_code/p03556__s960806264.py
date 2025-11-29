v1 = int(input())
v2 = 1
for v3 in range(v1):
    if v3 ** 2 <= v1:
        v2 = v3 ** 2
    else:
        break
print(v2)
