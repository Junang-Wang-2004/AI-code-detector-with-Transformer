v1 = int(input())
v2 = v1 % 10
if v2 == 2 or v2 == 4 or v2 == 5 or (v2 == 7) or (v2 == 9):
    print('hon')
elif v2 == 0 or v2 == 1 or v2 == 6 or (v2 == 8):
    print('pon')
elif v2 == 3:
    print('bon')
