v1 = input()
v2 = [int(x) for v3 in v1]
for v4 in range(min(set(v2)), max(set(v2)) + 1):
    v5 = int(str(v4) * 3)
    if v5 >= int(v1):
        print(v5)
        break
