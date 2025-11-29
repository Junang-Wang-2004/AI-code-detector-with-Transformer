class C1:

    def minOperations(self, a1):

        def search_insert(a1, a2):
            v1 = 0
            v2 = len(a1)
            while v1 < v2:
                v3 = v1 + (v2 - v1) // 2
                if a1[v3] <= a2:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1
        v1 = []
        for v2 in a1:
            v3 = search_insert(v1, -v2)
            if v3 == len(v1):
                v1.append(-v2)
            else:
                v1[v3] = -v2
        return len(v1)
