class C1(object):

    def countComponents(self, a1, a2):
        """
        """
        v1 = UnionFind(a2)
        v2 = [-1] * a2
        for v3 in a1:
            if v3 - 1 >= a2:
                continue
            for v4 in range(v3 + v3, a2 + 1, v3):
                v1.union_set(v4 - 1, v3 - 1)
        return sum((v3 - 1 >= a2 or v1.find_set(v3 - 1) == v3 - 1 for v3 in a1))
