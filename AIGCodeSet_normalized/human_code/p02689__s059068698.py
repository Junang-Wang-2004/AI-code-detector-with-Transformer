v1, v2 = list(map(int, input().split()))

class C1:

    def __init__(self, a1, a2):
        self.elevation = a1
        self.roads_connecting = []
        self.id = a2

    def __repr__(self):
        return 'ID:' + str(self.id) + ' E:' + str(self.elevation) + 'm'
v3 = input().split()
v4 = []
v5 = 1
for v6 in v3:
    v4.append(C1(int(v6), v5))
    v5 += 1
for v7 in range(v2):
    v8 = list(map(int, input().split()))
    v4[v8[0] - 1].roads_connecting.append(v4[v8[1] - 1])
    v4[v8[1] - 1].roads_connecting.append(v4[v8[0] - 1])
v9 = 0
for v10 in v4:
    v11 = True
    if len(set(v10.roads_connecting)) == 0:
        v9 += 1
        continue
    for v12 in set(v10.roads_connecting):
        if v12.elevation >= v10.elevation and v12.id != v10.id:
            v11 = False
            break
    if v11:
        v9 += 1
print(v9)
