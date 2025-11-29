v1 = [5, 5, 7]
v2 = list(map(int, input().split()))
v2.sort()
for v3 in range(3):
    if v2[v3] != v1[v3]:
        print('NO')
        exit()
print('YES')
