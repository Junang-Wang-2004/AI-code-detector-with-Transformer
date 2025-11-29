v1 = int(input())
list = []
v2 = input().split()
for v3 in range(0, len(v2)):
    list.append(int(v2[v3]))
v4 = True
for v5 in list:
    if v5 % 2 == 0 and (v5 % 3 != 0 and v5 % 5 != 0):
        v4 = False
        break
if v4:
    print('APPROVED')
else:
    print('DENIED')
