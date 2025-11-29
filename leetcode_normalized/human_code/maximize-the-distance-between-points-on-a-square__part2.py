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
            for v3 in range(1, len(sorted_points)):
                v4, v5 = (v3, 1)
                while v2 < len(v1):
                    v6, v7, v8 = v1[v2]
                    if abs(sorted_points[v3][0] - sorted_points[v7][0]) + abs(sorted_points[v3][1] - sorted_points[v7][1]) < a1:
                        break
                    if abs(sorted_points[v3][0] - sorted_points[v6][0]) + abs(sorted_points[v3][1] - sorted_points[v6][1]) >= a1:
                        if v8 + 1 >= v5:
                            v5 = v8 + 1
                            v4 = v6
                    v2 += 1
                v1.append((v4, v3, v5))
            return max((x[2] for v9 in v1)) >= a3
        v1 = [[] for v2 in range(4)]
        for v3, v4 in a2:
            if v3 == 0:
                v1[0].append((v3, v4))
            elif v4 == a1:
                v1[1].append((v3, v4))
            elif v3 == a1:
                v1[2].append((v3, v4))
            else:
                v1[3].append((v3, v4))
        v1[0].sort()
        v1[1].sort()
        v1[2].sort(reverse=True)
        v1[3].sort(reverse=True)
        v5 = [v3 for v6 in range(4) for v3 in v1[v6]]
        return binary_search_right(1, 4 * a1 // a3, check)
