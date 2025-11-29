v1 = list(map(int, str(input())))
v2 = [2, 4, 5, 7, 9]
v3 = [0, 1, 6, 8]
if v1[-1] in v2:
    print('hon')
elif v1[-1] in v3:
    print('pon')
else:
    print('bon')
