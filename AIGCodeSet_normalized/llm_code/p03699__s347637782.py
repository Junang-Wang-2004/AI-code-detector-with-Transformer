v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = True
for v5 in range(len(v2)):
    if v2[v5] % 10 != 0:
        v4 = False
        break
if v4:
    print(0)
else:
    v2.sort()
    v2 = v2[::-1]
    v6 = 2 ** len(v2)
    for v7 in range(v6):
        v8 = 0
        v9 = format(v7, 'b').zfill(len(v2))
        for v5 in range(len(v2)):
            print('combination', v5, v9[v5])
            if v9[v5] == '0':
                v8 += v2[v5]
        if v8 % 10 != 0:
            break
    print(v8)
