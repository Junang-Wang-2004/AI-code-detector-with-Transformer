from queue import Queue
v1 = input().split(' ')
v2 = int(v1[0])
v3 = int(v1[1])
v4 = []
v5 = []
for v6 in range(v3):
    v1 = input().split(' ')
    v4.append(int(v1[0]))
    v5.append(int(v1[1]))
    v4.append(int(v1[1]))
    v5.append(int(v1[0]))
v7 = {}
v8 = {}
v9 = {}
v10 = Queue(v2)
for v6, v11 in enumerate(v5):
    if v5[v6] == 1:
        v8[v4[v6]] = 1
v7.update(v8)
while True:
    for v12 in v8:
        for v6, v11 in enumerate(v5):
            if v11 == v12 and v4[v6] not in v9 and (v4[v6] not in v7) and (v4[v6] != 1):
                v9[v4[v6]] = v12
    if len(v9) == 0:
        break
    else:
        v8.clear()
        v8.update(v9)
        v7.update(v9)
        v9.clear()
print(v7)
if len(v7) == v2 - 1:
    print('Yes')
    for v13 in v7:
        print(v7[v13])
else:
    print('No')
