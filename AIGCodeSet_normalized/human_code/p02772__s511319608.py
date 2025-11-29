v1 = int(input())
v2 = list(map(int, input().split()))
for v3 in range(v1):
    if v2[v3] % 2 == 0:
        if not (v2[v3] % 3 == 0 or v2[v3] % 5 == 0):
            print('DENIED')
            exit()
else:
    print('APPROVED')
