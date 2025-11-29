v1 = input()
v2 = int(input())
v3 = len(v1)
v4 = v3 // v2 + 1
v5 = []
for v6 in range(v4):
    v5.append(v1[v2 * v6:v2 * v6 + v2])
for v7 in v5:
    try:
        print(v7[0], end='')
    except IndexError:
        pass
