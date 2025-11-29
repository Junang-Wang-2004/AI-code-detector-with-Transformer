import math
v1 = int(input())
v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v3 = 0
while True:
    if len(v2) == v1:
        print(v2[v1 - 1])
        break
    v3 = v3 + 1
    v4 = str(v3)
    v5 = True
    for v6 in range(len(v4) - 1):
        if abs(int(v4[v6]) - int(v4[v6 + 1])) > 1:
            v5 = False
            break
    if v5:
        v2.append(v3)
print(v2)
