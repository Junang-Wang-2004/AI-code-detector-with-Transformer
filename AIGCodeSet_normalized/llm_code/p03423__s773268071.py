v1 = int(input())
if v1 % 3 == 0:
    print(v1 // 3)
elif v1 % 3 == 1:
    print(v1 // 3 - 1)
else:
    print(v1 // 3 + 1)
