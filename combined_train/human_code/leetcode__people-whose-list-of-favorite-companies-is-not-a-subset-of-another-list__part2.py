class C1(object):

    def __init__(self, a1):
        self.data = [set(d) for v1 in a1]
        self.set = list(range(len(a1)))

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return
        if len(self.data[v1]) > len(self.data[v2]) and self.data[v1] > self.data[v2]:
            self.set[v2] = v1
        elif len(self.data[v1]) < len(self.data[v2]) and self.data[v1] < self.data[v2]:
            self.set[v1] = v2

class C2(object):

    def peopleIndexes(self, a1):
        """
        """
        v1, v2 = ({}, [])
        for v3 in a1:
            v2.append(set())
            for v4 in v3:
                if v4 not in v1:
                    v1[v4] = len(v1)
                v2[-1].add(v1[v4])
        v5 = C1(v2)
        for v6 in range(len(v2)):
            for v7 in range(len(v2)):
                if v7 == v6:
                    continue
                v5.union_set(v6, v7)
        return [x for v6, v8 in enumerate(v5.set) if v8 == v6]
