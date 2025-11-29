v1 = int(input())
v2 = set()
for v3 in range(v1):
    v4 = int(input())
    if v4 in v2:
        v2.remove(v4)
    else:
        v2.add(v4)
print(len(v2))
