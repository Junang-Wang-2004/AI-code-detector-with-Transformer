from bisect import insort_left, bisect_left
v1 = int(input())
v2 = input()
v3 = int(input())
v4 = 'abcdefghijklmnopqrstuvwxyz'
v5 = {i: [-1, v1 + 1] for v6 in v4}
for v6 in range(v1):
    insort_left(v5[v2[v6]], v6)
for v6 in range(v3):
    v7, v8, v9 = input().split()
    if v7 == '1':
        v8 = int(v8) - 1
        v10 = bisect_left(v5[v2[v8]], v8)
        v5[v2[v8]].pop(v10)
        insort_left(v5[v9], v8)
    else:
        v8, v9 = (int(v8) - 1, int(v9) - 1)
        v11 = 0
        for v6 in v4:
            v12 = bisect_left(v5[v6], v8)
            if v12 >= len(v5[v6]):
                continue
            elif v5[v6][v12] <= v9:
                v11 += 1
        print(v11)
