v1 = int(input())
v2 = [2, 4, 5, 7, 9]
v3 = [3]
v4 = [0, 1, 6, 8]
if v1 % 10 in v2:
    print(str(v1) + 'hon')
elif v1 % 10 in v3:
    print(str(v1) + 'bon')
else:
    print(str(v1) + 'pon')
