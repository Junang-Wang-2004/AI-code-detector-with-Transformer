v1 = input()
v2 = list(map(int, input().split()))
v3 = True
for v4 in range(0, len(v2)):
    if v2[v4] % 2 == 0 and (v2[v4] % 3 != 0 and v2[v4] % 5 != 0):
        v3 = False
        break
if v3 == True:
    print('APPROVED')
else:
    print('DENIED')
