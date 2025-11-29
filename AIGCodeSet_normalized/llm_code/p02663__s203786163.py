import readline
import datetime
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())
while 0 <= v1 < 23 and 0 <= v2 < 60 and (0 <= v3 < 23) and (0 <= v4 < 60):
    if v4 > v2:
        v6 = (v3 - v1) * 60 + v4 - v2
        print(v6 - v5)
    else:
        v4 < v2
        v7 = (v3 - v1) * 60 + v2 - v4
        print(v7 - v5)
else:
    print('Invalid input')
