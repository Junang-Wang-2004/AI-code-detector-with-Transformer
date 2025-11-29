v1, v2 = map(int, input().split())
v3 = [1]
for v4 in range(2, 1000):
    v3.append(v3[v4 - 2] + v4)
    if v1 < v3[v4 - 1]:
        print(v3[v4 - 1] - v1)
        break
