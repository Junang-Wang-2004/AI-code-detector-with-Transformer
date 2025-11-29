class C1:

    def __init__(self, a1, a2, a3):
        self.hp = a1
        self.live = 1
        self.center = a2
        self.side = a3

    def is_die(self):
        if self.hp <= 0:
            self.live = 0

    def center_bombed(self):
        self.hp -= self.center
        self.is_die()

    def side_bombed(self):
        self.hp -= self.side
        self.is_die()
v1, v2, v3 = [int(i) for v4 in input().split()]
v5 = []
v6 = 0
for v4 in range(v1):
    v7 = int(input())
    v5.append(C1(v7, v2, v3))
while True:
    v8 = len(v5)
    v9 = [m.hp for v10 in v5]
    v11 = max(v9)
    v12 = v9.index(v11)
    for v4 in range(v8):
        if v4 == v12:
            v5[v4].center_bombed()
        else:
            v5[v4].side_bombed()
    v6 += 1
    v5 = [v10 for v10 in v5 if v10.live == 1]
    if len(v5) == 0:
        print(v6)
        break
