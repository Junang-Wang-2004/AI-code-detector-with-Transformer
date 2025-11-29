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

    def countComponents(self, a1, a2):
        """
        """
        v1 = C1(a1)
        for v2, v3 in a2:
            v1.union_set(v2, v3)
        return v1.count
