if (i * (i + 1) // 2 - x) % i == 0:
    print(i + 1)
    break
v1 = int(input())
for v2 in range(v1 ** 0.5 + 100):
    if v2 * (v2 + 1) // 2 >= v1:
        print(v2)
        break
    elif (v2 * (v2 + 1) // 2 - v1) % v2 == 0:
        print(v2 + 1)
        break
