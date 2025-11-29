class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        return True

class C2(object):

    def canReachCorner(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4, a5, a6):
            return (a1 - a4) ** 2 + (a2 - a5) ** 2 <= (a3 + a6) ** 2
        v1 = C1(len(a3) + 2)
        for v2 in range(len(a3)):
            v3, v4, v5 = a3[v2]
            if v3 - v5 <= 0 or v4 + v5 >= a2:
                v1.union_set(v2, len(a3))
            if v3 + v5 >= a1 or v4 - v5 <= 0:
                v1.union_set(v2, len(a3) + 1)
            for v6 in range(v2):
                v7, v8, v9 = a3[v6]
                if not check(v3, v4, v5, v7, v8, v9):
                    continue
                v1.union_set(v2, v6)
        return v1.find_set(len(a3)) != v1.find_set(len(a3) + 1)
