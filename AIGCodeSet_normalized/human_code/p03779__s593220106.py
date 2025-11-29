v1 = int(input())
for v2 in range(1, v1 + 1):
    if v2 * (v2 + 1) * 0.5 >= v1:
        print(v2)
        break
