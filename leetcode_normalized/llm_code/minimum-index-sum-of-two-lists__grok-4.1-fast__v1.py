class C1:

    def findRestaurant(self, a1, a2):
        v1 = {}
        for v2, v3 in enumerate(a1):
            v1[v3] = v2
        v4 = float('inf')
        for v2, v3 in enumerate(a2):
            if v3 in v1:
                v5 = v1[v3] + v2
                if v5 < v4:
                    v4 = v5
        v6 = []
        for v2, v3 in enumerate(a2):
            if v2 > v4:
                break
            if v3 in v1 and v1[v3] + v2 == v4:
                v6.append(v3)
        return v6
