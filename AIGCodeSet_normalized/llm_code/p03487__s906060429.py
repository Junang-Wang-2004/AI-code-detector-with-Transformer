v1 = 0
v2 = list(map(int, input().split()))
for v3 in set(v2):
    while True:
        if v2.count(v3) == 0 or v2.count(v3) == v3:
            break
        v2.remove(v3)
        v1 += 1
print(v1)
