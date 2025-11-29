v1 = int(input())
v2 = int(input())
if v1 % (2 * v2) == 0:
    print(v1 // (2 * v2))
else:
    print(v1 // (2 * v2) + 1)
