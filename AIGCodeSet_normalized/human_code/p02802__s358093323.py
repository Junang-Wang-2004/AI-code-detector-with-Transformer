import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split(' '))
v3 = [0] * v1
v4 = 0
v5 = 0
for v6 in range(v2):
    v7, v8 = input().strip().split(' ')
    v7 = int(v7) - 1
    if v3[v7] == -1:
        continue
    if v8 == 'AC':
        v5 += v3[v7]
        v4 += 1
        v3[v7] = -1
    else:
        v3[v7] += 1
print(v4, v5)
