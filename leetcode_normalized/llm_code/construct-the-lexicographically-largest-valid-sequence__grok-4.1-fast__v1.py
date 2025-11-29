class C1:

    def constructDistancedSequence(self, a1):
        v1 = 2 * a1 - 1
        v2 = [0] * v1
        v3 = set()

        def search(a1):
            if a1 == v1:
                return True
            if v2[a1] != 0:
                return search(a1 + 1)
            for v1 in range(a1, 0, -1):
                if v1 in v3:
                    continue
                v2 = a1 + v1
                if v1 > 1 and (v2 >= v1 or v2[v2] != 0):
                    continue
                v2[a1] = v1
                if v1 > 1:
                    v2[v2] = v1
                v3.add(v1)
                if search(a1 + 1):
                    return True
                v2[a1] = 0
                if v1 > 1:
                    v2[v2] = 0
                v3.remove(v1)
            return False
        search(0)
        return v2
