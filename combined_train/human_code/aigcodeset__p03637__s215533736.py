v1 = int(input())
list = input().split()
v2 = []
v3 = []
v4 = []
for v5 in range(0, v1):
    if int(list[v5]) % 2 != 0:
        v2.append(list[v5])
    elif int(list[v5]) % 2 == 0 and int(list[v5]) % 4 != 0:
        v3.append(list[v5])
    elif int(list[v5]) % 4 == 0:
        v4.append(list[v5])
v6 = len(v2)
v7 = len(v3)
v8 = len(v4)
if v8 >= v6 - 1 and v7 == 0:
    print('Yes')
elif v8 >= v6:
    print('Yes')
else:
    print('No')
