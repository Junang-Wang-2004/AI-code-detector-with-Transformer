class C1(object):

    def maxDistance(self, a1, a2, a3):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def check(a1):
            v1 = [(0, 0, 1)]
            v2 = 0
            for v3 in range(1, len(p)):
                v4, v5 = (v3, 1)
                while v2 < len(v1):
                    v6, v7, v8 = v1[v2]
                    if p[v3] - p[v7] < a1:
                        break
                    if p[v6] + 4 * a1 - p[v3] >= a1:
                        if v8 + 1 >= v5:
                            v5 = v8 + 1
                            v4 = v6
                    v2 += 1
                v1.append((v4, v3, v5))
            return max((x[2] for v9 in v1)) >= a3
        v1 = []
        for v2, v3 in a2:
            if v2 == 0:
                v1.append(0 * a1 + v3)
            elif v3 == a1:
                v1.append(1 * a1 + v2)
            elif v2 == a1:
                v1.append(2 * a1 + (a1 - v3))
            else:
                v1.append(3 * a1 + (a1 - v2))
        v1.sort()
        return binary_search_right(1, 4 * a1 // a3, check)
