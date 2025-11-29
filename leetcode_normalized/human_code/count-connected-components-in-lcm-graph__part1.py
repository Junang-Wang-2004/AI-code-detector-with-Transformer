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

    def countComponents(self, a1, a2):
        """
        """
        v1 = C1(a2)
        v2 = [-1] * a2
        v3 = len(a1)
        for v4 in a1:
            if v4 - 1 >= a2:
                continue
            for v5 in range(v4, a2 + 1, v4):
                if v2[v5 - 1] == -1:
                    v2[v5 - 1] = v4 - 1
                    continue
                if v1.union_set(v2[v5 - 1], v4 - 1):
                    v3 -= 1
                if v5 == v4:
                    break
        return v3
