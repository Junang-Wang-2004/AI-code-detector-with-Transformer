v1, v2 = (list(), list())
for v3 in range(int(input())):
    v4, v5 = map(int, input().split())
    v1.append([v4, v5])
    v2.append([v5, v4])
(v1.sort(), v2.sort())
print(max(v1[-1][0] - v1[0][0] + v1[-1][1] - v1[0][1], v2[-1][0] - v2[0][0] + v2[-1][1] - v2[0][1]))
