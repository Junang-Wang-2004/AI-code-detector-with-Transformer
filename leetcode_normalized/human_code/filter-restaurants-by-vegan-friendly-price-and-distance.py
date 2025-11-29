class C1(object):

    def filterRestaurants(self, a1, a2, a3, a4):
        """
        """
        v1, v2 = ([], {})
        for v3, (v4, v5, v6, v7, v8) in enumerate(a1):
            if v6 >= a2 and v7 <= a3 and (v8 <= a4):
                v2[v4] = v3
                v1.append(v4)
        v1.sort(key=lambda i: (-a1[v2[v4]][1], -a1[v2[v4]][0]))
        return v1
