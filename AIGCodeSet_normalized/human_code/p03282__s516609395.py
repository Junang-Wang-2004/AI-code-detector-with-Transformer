import sys
input = sys.stdin.readline
v1 = list(map(int, list(input())[:-1]))
v2 = int(input())
v3 = 0
for v4 in range(len(v1)):
    if v1[v4] == 1:
        v3 += 1
    else:
        break
if v2 <= v3:
    print(1)
else:
    print(v1[v3])
