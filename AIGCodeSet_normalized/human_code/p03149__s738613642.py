from sys import stdin
v1 = stdin.readline().rstrip().split()
v2 = 0
for v3 in [1, 9, 7, 4]:
    if str(v3) not in v1:
        print('NO')
        v2 = 1
        break
if v2 == 0:
    print('YES')
