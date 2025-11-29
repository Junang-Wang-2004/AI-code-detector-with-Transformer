v1 = int(input())
if v1 == 1 or v1 == 2:
    print(4)
else:

    def f1(a1):
        if a1 % 2 == 0:
            return int(a1 / 2)
        else:
            return 3 * a1 + 1
    v2 = []
    v3 = v1
    while v3 != 1:
        v2.append(v3)
        v3 = f1(v3)
    print(len(v2) + 2)
