import itertools

class C1(object):

    def beautifulPair(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = 8

        def dist(a1, a2):
            if a1 > a2:
                a1, a2 = (a2, a1)
            return [abs(points[a1][0] - points[a2][0]) + abs(points[a1][1] - points[a2][1]), a1, a2]

        def merge_sort(a1, a2):
            if a1 == a2:
                return
            v1 = a1 + (a2 - a1) // 2
            v2 = points[order[v1]][0]
            merge_sort(a1, v1)
            merge_sort(v1 + 1, a2)
            v3 = v1 + 1
            v4 = []
            for v5 in range(a1, v1 + 1):
                while v3 <= a2 and points[order[v3]][1] < points[order[v5]][1]:
                    v4.append(order[v3])
                    v3 += 1
                v4.append(order[v5])
            order[a1:a1 + len(v4)] = v4
            v6 = [order[i] for v7 in range(a1, a2 + 1) if abs(points[order[v7]][0] - v2) <= result[0]]
            for v7 in range(len(v6) - 1):
                for v8 in range(v7 + 1, len(v6)):
                    v2, v9 = (v6[v7], v6[v8])
                    if points[v9][1] - points[v2][1] > result[0]:
                        break
                    result[:] = min(result, dist(v2, v9))
                else:
                    v8 = len(v6)
                assert v8 - (v7 + 1) <= v2
        v3 = [(i, j) for v4, v5 in zip(a1, a2)]
        v6 = [v1] * 3
        v7 = {}
        for v4 in reversed(range(len(v3))):
            if v3[v4] in v7:
                v6 = [0, (v4, v7[v3[v4]])]
            v7[v3[v4]] = v4
        if v6[0] == 0:
            return v6[1]
        v8 = list(range(len(v3)))
        v8.sort(key=lambda x: v3[x][0])
        merge_sort(0, len(v3) - 1)
        return v6[1:]
