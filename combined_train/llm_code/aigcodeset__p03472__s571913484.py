v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v3 = numpy.array(v3)
v4 = numpy.array(v4)
v8 = numpy.sort(v3)[::-1]
v9 = numpy.sort(v4)[::-1]
v10 = 0
v11 = v8[0]
v12 = v9[v11 < v9]
if sum(v12) >= v2:
    for v5 in range(1, len(v12) + 1)[::-1]:
        if sum(v12[:v5]) < v2:
            v10 = v5 + 1
            break
else:
    v13 = v2 - sum(v12)
    v14 = int(numpy.ceil(v13 / v11))
    v10 = v14 + len(v12)
print(v10)
