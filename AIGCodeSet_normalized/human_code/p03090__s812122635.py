v1 = int(input())
if v1 & 1:
    print(v1 * (v1 - 2) // 2 + 1)
    for v2 in range(1, v1):
        for v3 in range(v2 + 1, v1 + 1):
            if v3 + v2 != v1:
                print(v2, v3)
else:
    print(v1 * (v1 - 2) // 2)
    for v2 in range(1, v1):
        for v3 in range(v2 + 1, v1 + 1):
            if v3 + v2 != v1 + 1:
                print(v2, v3)
