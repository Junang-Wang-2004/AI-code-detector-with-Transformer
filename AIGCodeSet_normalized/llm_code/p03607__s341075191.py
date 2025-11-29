v1 = []
v2 = int(input())
for v3 in range(v2):
    v4 = int(input())
    if v4 in v1:
        v1.remove(v4)
    else:
        v1.append(v4)
print(len(v1))
