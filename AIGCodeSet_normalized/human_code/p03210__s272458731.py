import sys
v1 = int(input())
if not 1 <= v1 <= 9:
    sys.exit()
print('YES') if v1 == 3 or v1 == 5 or v1 == 7 else print('NO')
