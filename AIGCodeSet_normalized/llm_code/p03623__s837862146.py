import sys
import itertools
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
v4, v5, v6 = map(int, v1().split())
print('A' if abs(v4 - v5) < abs(v4 - v6) else 'B')
