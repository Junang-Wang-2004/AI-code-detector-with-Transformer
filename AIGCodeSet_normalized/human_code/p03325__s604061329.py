v1, *v2 = map(int, open(0).read().split())
v3 = 0
for v4 in v2:
    while True:
        v4, v5 = divmod(v4, 2)
        if v5 == 1:
            break
        v3 += 1
print(v3)
