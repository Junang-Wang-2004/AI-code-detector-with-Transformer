v1 = int(input())
if v1 % 1000 == 0:
    print(0)
else:
    print(1000 - v1 % 1000)
