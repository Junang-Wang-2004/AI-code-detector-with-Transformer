v1 = int(input())
v2 = False
for v3 in range(1, v1 + 1):
    v4 = v3 + int(v3 * 0.08)
    if v4 == v1:
        print(v3)
        v2 = True
        break
if not v2:
    print(':(')
