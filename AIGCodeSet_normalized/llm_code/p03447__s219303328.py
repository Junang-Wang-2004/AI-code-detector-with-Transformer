import sys
input = sys.stdin.readline
v1 = int(input())
v2 = int(input())
v3 = int(input())
v1 -= v2
print(v1 - v1 // v3 * v3)
