"""input
3
1
30000
20000
"""
import time
import math
v1 = int(input())
print('second' if all([int(input()) % 2 == 0 for v2 in range(v1)]) else 'first')
