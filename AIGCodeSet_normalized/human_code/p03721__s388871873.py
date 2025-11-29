v1, v2 = map(int, input().split(' '))
v3 = [tuple(map(int, input().split(' '))) for v4 in range(v1)]
v3 = sorted(v3, key=lambda x: x[0])
v5 = 0
v4 = 0
while True:
    v5 = v5 + v3[v4][1]
    if v5 >= v2:
        break
    v4 = v4 + 1
print(v3[v4][0])
