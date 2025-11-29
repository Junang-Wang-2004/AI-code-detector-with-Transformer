v1 = int(input())
v2 = []
v3 = []
v4 = []
for v5 in range(v1):
    v6 = int(input())
    if v6 < 30000:
        v7 = v6
        if v7 in v2:
            v2.remove(v7)
        else:
            v2.append(v7)
    elif 30001 <= v6 < 70000:
        v8 = v6
        if v8 in v3:
            v3.remove(v8)
        else:
            v3.append(v8)
    else:
        v9 = v6
        if v9 in v4:
            v4.remove(v9)
        else:
            v4.append(v9)
print(len(v2) + len(v3) + len(v4))
