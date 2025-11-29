class C1:

    def firstUniqChar(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        for v3, v2 in enumerate(a1):
            if v1[v2] == 1:
                return v3
        return -1
