v1 = int(input())
v2 = 0
for v3 in range(1, 10 ** 9):
    v2 += v3
    if v2 >= v1:
        print(v3)
        break
