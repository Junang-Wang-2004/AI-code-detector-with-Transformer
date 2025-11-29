v1 = int(input())
v2 = []
for v3 in range(10 ** 6):
    if v1 % 2 == 0:
        v1 //= 2
    else:
        v1 = 3 * v1 + 1
    v2.append(v1)
    if len(set(v2)) != v3 + 1:
        print(v3 + 2)
        break
