v1 = int(input())
v2 = list(map(int, input().split()))
for v3 in v2:
    if v3 % 2 == 0 and (v3 % 3 != 0 and v3 % 5 != 0):
        print('DENIED')
        exit()
print('APPROVED')
