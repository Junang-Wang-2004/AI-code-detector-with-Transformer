import sys
input = sys.stdin.readline
v1 = int(input())
v2, v3 = ([], [])
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append(v5 + v6)
    v3.append(v5 - v6)
v2.sort()
v3.sort()
print(max(abs(v2[0] - v2[-1]), abs(v3[0] - v3[-1])))
