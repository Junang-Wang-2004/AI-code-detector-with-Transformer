v1 = int(input())
if v1 % 10 == 3:
    print('bon')
elif v1 % 10 == 0 or v1 % 10 == 1 or v1 % 10 == 6 or (v1 % 10 == 8):
    print('pon')
else:
    print('hon')
