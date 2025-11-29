class C1(object):

    def findRestaurant(self, a1, a2):
        """
        """
        v1 = {}
        for v2, v3 in enumerate(a1):
            v1[v3] = v2
        v4 = []
        v5 = float('inf')
        for v6, v3 in enumerate(a2):
            if v6 > v5:
                break
            if v3 in v1:
                if v6 + v1[v3] < v5:
                    v4 = [v3]
                    v5 = v6 + v1[v3]
                elif v6 + v1[v3] == v5:
                    v4.append(v3)
        return v4
