import sys
v1, v2 = map(int, input().split())
v3 = input()
v4 = v1
v5 = []
while v4 > 0:
    for v6 in range(max(0, v4 - v2), v4):
        if v3[v6] == '0':
            v5.append(v4 - v6)
            v4 = v6
            break
    else:
        print(-1)
        sys.exit()
print(*v5[::-1])
