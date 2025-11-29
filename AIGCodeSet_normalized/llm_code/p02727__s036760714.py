v1, v2, v3, v4, v5 = map(int, input().split())
v6 = list(map(int, input().split()))
v7 = list(map(int, input().split()))
v8 = list(map(int, input().split()))
v6.sort(reverse=True)
v7.sort(reverse=True)
v8.sort(reverse=True)
v9 = v6[:v1] + v7[:v2]
v9.sort(reverse=True)
v10 = 0
for v11 in range(len(v9)):
    if v10 < v5 and v9[v11] < v8[v10]:
        v9[v11] = v8[v10]
        v10 += 1
    else:
        continue
print(sum(v9))
