class C1:

    def validPath(self, a1, a2, a3, a4):
        v1 = list(range(a1))
        v2 = [1] * a1

        def root(a1):
            v1 = a1
            while v1[v1] != v1:
                v1 = v1[v1]
            while a1 != v1:
                v2 = v1[a1]
                v1[a1] = v1
                a1 = v2
            return v1

        def merge(a1, a2):
            v1, v2 = (root(a1), root(a2))
            if v1 == v2:
                return
            if v2[v1] < v2[v2]:
                v1[v1] = v2
                v2[v2] += v2[v1]
            else:
                v1[v2] = v1
                v2[v1] += v2[v2]
        for v3, v4 in a2:
            merge(v3, v4)
        return root(a3) == root(a4)
