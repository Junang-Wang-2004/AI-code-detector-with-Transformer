list = input().split()
if int(list[0]) >= 10:
    print(int(list[1]))
else:
    print(int(list[1]) + 100 * (10 - int(list[0])))
