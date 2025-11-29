v1, v2, v3 = map(int, input().split())
v4 = list(input())
v5 = 0
v6 = 0
for v7 in range(v1):
    if v4[v7] == 'a' and v5 < v2 + v3:
        print('Yes')
        v5 += 1
    elif v4[v7] == 'b' and v5 < v2 + v3 and (v6 <= v3):
        print('Yes')
        v6 += 1
    else:
        print('No')
