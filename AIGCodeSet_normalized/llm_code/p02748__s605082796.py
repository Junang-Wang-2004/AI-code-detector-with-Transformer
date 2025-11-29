v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = []
for v7 in range(v3):
    v6.append(list(map(int, input().split())))
v8 = v4.sort()[0]
v9 = v5.sort()[0]
min = v8 + v9
v10 = [min]
for list in v6:
    v11 = a_list[list[0] - 1] + b_list[list[1] - 1] - list[2]
    v10.append(v11)
v10.sort()
v12 = v10[0]
print(v12)
