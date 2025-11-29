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

    def numIslands(self, a1):
        """
        """

        def index(a1, a2, a3):
            return a2 * a1 + a3
        if not a1:
            return 0
        v1 = 0
        v2 = C1(len(a1) * len(a1[0]))
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4] == '1':
                    if v3 and a1[v3 - 1][v4] == '1':
                        v2.union_set(index(len(a1[0]), v3 - 1, v4), index(len(a1[0]), v3, v4))
                    if v4 and a1[v3][v4 - 1] == '1':
                        v2.union_set(index(len(a1[0]), v3, v4 - 1), index(len(a1[0]), v3, v4))
                else:
                    v1 += 1
        return v2.count - v1
