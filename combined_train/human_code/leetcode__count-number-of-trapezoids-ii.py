import collections

class C1(object):

    def countTrapezoids(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return abs(a1)
        v1 = collections.defaultdict(int)
        v2 = collections.defaultdict(int)
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)
        v5 = v6 = 0
        for v7 in range(len(a1)):
            v8, v9 = a1[v7]
            for v10 in range(v7):
                v11, v12 = a1[v10]
                v13, v14 = (v11 - v8, v12 - v9)
                v15 = gcd(v13, v14)
                v16, v17 = (v13 // v15, v14 // v15)
                if v16 < 0 or (v16 == 0 and v17 < 0):
                    v16, v17 = (-v16, -v17)
                v18 = v17 * v8 - v16 * v9
                v5 += v1[v16, v17] - v2[v16, v17, v18]
                v1[v16, v17] += 1
                v2[v16, v17, v18] += 1
                v19 = v13 ** 2 + v14 ** 2
                v6 += v3[v16, v17, v19] - v4[v16, v17, v18, v19]
                v3[v16, v17, v19] += 1
                v4[v16, v17, v18, v19] += 1
        return v5 - v6 // 2
