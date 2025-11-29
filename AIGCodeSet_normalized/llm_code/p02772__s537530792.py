v1 = list(map(int, input().split()))
v2 = 0
for v3 in v1:
    if v3 % 2 == 0 and (v3 % 3 == 0 or v3 % 5 == 0):
        v2 = 1
if v2 == 0:
    print('APPROVED')
else:
    print('DENIED')
