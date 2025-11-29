v1 = int(input())
v2 = v1 % 10
if v2 in [2, 4, 5, 7, 9]:
    print(v1, 'hon')
elif v2 in [0, 1, 6, 8]:
    print(v1, 'pon')
else:
    print(v1, 'bon')
