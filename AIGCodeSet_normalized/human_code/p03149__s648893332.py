import math
import itertools
import sys
import copy
v1 = list(map(int, input().split()))
v1.sort()
if v1[0] == 1 and v1[1] == 4 and (v1[2] == 7) and (v1[3] == 9):
    print('YES')
else:
    print('NO')
