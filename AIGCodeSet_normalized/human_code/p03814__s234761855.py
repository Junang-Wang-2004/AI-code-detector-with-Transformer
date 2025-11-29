v1 = input()
v2 = None
v3 = 0
for v4, v5 in enumerate(v1):
    if v5 == 'A' and v2 is None:
        v2 = v4
    if v5 == 'Z':
        v3 = v4
print(v3 - v2 + 1)
