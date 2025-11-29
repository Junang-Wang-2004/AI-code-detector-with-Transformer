import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
v1 = int(input())
v2 = input()
v3 = len(v2)
v4 = v1 + v3
v5 = 10 ** 9 + 7
v6 = pow(26, v4, v5)

class C1:

    def __init__(self):
        self.power = 1
        self.rev = 1

class C2:

    def __init__(self, a1, a2):
        self.lists = [C1() for v1 in range(a1 + 1)]
        self.mod = a2
        for v2 in range(2, a1 + 1):
            self.lists[v2].power = self.lists[v2 - 1].power * v2 % self.mod
        self.lists[a1].rev = pow(self.lists[a1].power, self.mod - 2, self.mod)
        for v3 in range(a1, 0, -1):
            self.lists[v3 - 1].rev = self.lists[v3].rev * v3 % self.mod

    def combi(self, a1, a2):
        if a1 < a2:
            return 0
        else:
            return self.lists[a1].power * self.lists[a1 - a2].rev * self.lists[a2].rev % self.mod
v7 = C2(2 * 10 ** 6 + 10000, v5)
for v8 in range(v3):
    v6 -= v7.combi(v4, v8) * pow(25, v4 - v8, v5)
    v6 %= v5
print(v6 % v5)
