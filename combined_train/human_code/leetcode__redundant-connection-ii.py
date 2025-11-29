class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        return True

class C2(object):

    def findRedundantDirectedConnection(self, a1):
        """
        """
        v1, v2 = ([], [])
        v3 = {}
        for v4 in a1:
            if v4[1] not in v3:
                v3[v4[1]] = v4[0]
            else:
                v1 = [v3[v4[1]], v4[1]]
                v2 = v4
        v5 = C1(len(a1) + 1)
        for v4 in a1:
            if v4 == v2:
                continue
            if not v5.union_set(*v4):
                return v1 if v2 else v4
        return v2
