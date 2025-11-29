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
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.set[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.set[v2] = v1
        else:
            self.set[v2] = v1
            self.rank[v1] += 1
        return True

class C2(object):

    def areConnected(self, a1, a2, a3):
        """
        """
        v1 = C1(a1)
        for v2 in range(a2 + 1, a1 + 1):
            for v3 in range(2 * v2, a1 + 1, v2):
                v1.union_set(v2 - 1, v3 - 1)
        return [v1.find_set(q[0] - 1) == v1.find_set(q[1] - 1) for v4 in a3]
