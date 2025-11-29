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

    def reset(self, a1):
        self.set[a1] = a1
        self.rank[a1] = 0

class C2(object):

    def findAllPeople(self, a1, a2, a3):
        """
        """
        a2.sort(key=lambda x: x[2])
        v1 = C1(a1)
        v1.union_set(0, a3)
        v2 = set()
        for v3, (v4, v5, v6) in enumerate(a2):
            v2.add(v4)
            v2.add(v5)
            v1.union_set(v4, v5)
            if v3 + 1 != len(a2) and a2[v3 + 1][2] == a2[v3][2]:
                continue
            while v2:
                v4 = v2.pop()
                if v1.find_set(v4) != v1.find_set(0):
                    v1.reset(v4)
        return [v3 for v3 in range(a1) if v1.find_set(v3) == v1.find_set(0)]
