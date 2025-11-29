class C1:

    def reconstructQueue(self, a1):
        v1 = sorted(a1, key=lambda x: (-x[0], x[1]))
        v2 = []
        for v3 in v1:
            v2.insert(v3[1], v3)
        return v2
