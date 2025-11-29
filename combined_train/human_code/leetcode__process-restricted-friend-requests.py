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

    def friendRequests(self, a1, a2, a3):
        """
        """
        v1 = []
        v2 = C1(a1)
        for v3, v4 in a3:
            v5, v6 = (v2.find_set(v3), v2.find_set(v4))
            v7 = True
            for v8, v9 in a2:
                v10, v11 = (v2.find_set(v8), v2.find_set(v9))
                if {v10, v11} == {v5, v6}:
                    v7 = False
                    break
            v1.append(v7)
            if v7:
                v2.union_set(v3, v4)
        return v1
