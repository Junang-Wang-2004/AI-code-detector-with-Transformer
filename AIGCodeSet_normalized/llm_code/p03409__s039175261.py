v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append((v5, v6))
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append((v5, v6))
v2.sort(key=lambda x: [x[0] + x[1], x[0], x[1]])
v3.sort(key=lambda x: [x[0] + x[1], x[0], x[1]])
v7 = 0
v8 = 0
while len(v3) > 0:
    v9 = v2.pop()
    for v10 in v3[::-1]:
        if v9[0] < v10[0] and v9[1] < v10[1]:
            v3.remove(v10)
            v7 += 1
            break
    else:
        pass
    v8 += 1
    if v8 >= 2 * v1:
        break
print(v7)
