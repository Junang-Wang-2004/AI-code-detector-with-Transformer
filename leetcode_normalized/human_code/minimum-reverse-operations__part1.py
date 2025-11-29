class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1
        self.right = list(range(a1))

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
        self.right[a2] = max(self.right[a1], self.right[a2])
        return True

    def right_set(self, a1):
        return self.right[self.find_set(a1)]

class C2(object):

    def minReverseOperations(self, a1, a2, a3, a4):
        """
        """
        v1 = [False] * a1
        for v2 in a3:
            v1[v2] = True
        v3 = 0
        v4 = [-1] * a1
        v4[a2] = v3
        v5 = C1(a1 + 2)
        v5.union_set(a2, a2 + 2)
        v6 = [a2]
        v3 += 1
        while v6:
            v7 = []
            for a2 in v6:
                v9, v10 = (2 * max(a2 - (a4 - 1), 0) + (a4 - 1) - a2, 2 * min(a2 + (a4 - 1), a1 - 1) - (a4 - 1) - a2)
                a2 = v5.right_set(v9)
                while a2 <= v10:
                    if not v1[a2]:
                        v4[a2] = v3
                        v7.append(a2)
                    v5.union_set(a2, a2 + 2)
                    a2 = v5.right_set(a2)
            v6 = v7
            v3 += 1
        return v4
