class C1:

    def validTree(self, a1, a2):
        if a1 == 0:
            return True
        v1 = list(range(a1))
        v2 = [0] * a1

        def get_root(a1):
            if v1[a1] != a1:
                v1[a1] = get_root(v1[a1])
            return v1[a1]

        def merge(a1, a2):
            v1, v2 = (get_root(a1), get_root(a2))
            if v1 == v2:
                return False
            if v2[v1] < v2[v2]:
                v1[v1] = v2
            elif v2[v1] > v2[v2]:
                v1[v2] = v1
            else:
                v1[v2] = v1
                v2[v1] += 1
            return True
        v3 = a1
        for v4, v5 in a2:
            if v4 >= a1 or v5 >= a1 or (not merge(v4, v5)):
                return False
            v3 -= 1
        return v3 == 1
