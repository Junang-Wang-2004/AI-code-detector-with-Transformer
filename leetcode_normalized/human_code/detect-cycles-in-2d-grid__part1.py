class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.count = a1

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 != v2:
            self.set[min(v1, v2)] = max(v1, v2)
            self.count -= 1

class C2(object):

    def containsCycle(self, a1):
        """
        """

        def index(a1, a2, a3):
            return a2 * a1 + a3
        v1 = C1(len(a1) * len(a1[0]))
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if v2 and v3 and (a1[v2][v3] == a1[v2 - 1][v3] == a1[v2][v3 - 1]) and (v1.find_set(index(len(a1[0]), v2 - 1, v3)) == v1.find_set(index(len(a1[0]), v2, v3 - 1))):
                    return True
                if v2 and a1[v2][v3] == a1[v2 - 1][v3]:
                    v1.union_set(index(len(a1[0]), v2 - 1, v3), index(len(a1[0]), v2, v3))
                if v3 and a1[v2][v3] == a1[v2][v3 - 1]:
                    v1.union_set(index(len(a1[0]), v2, v3 - 1), index(len(a1[0]), v2, v3))
        return False
