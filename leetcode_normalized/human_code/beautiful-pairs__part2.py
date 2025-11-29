import itertools

class C1(object):

    def beautifulPair(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = (8 + 2) // 2

        def dist(a1, a2):
            if a1 > a2:
                a1, a2 = (a2, a1)
            return [abs(points[a1][0] - points[a2][0]) + abs(points[a1][1] - points[a2][1]), a1, a2]

        def merge_sort(a1, a2):

            def update(a1, a2):
                for v1 in reversed(range(len(a1))):
                    if points[a2][1] - points[a1[v1]][1] > result[0]:
                        break
                    result[:] = min(result, dist(a2, a1[v1]))
                else:
                    v1 = -1
                assert len(a1) - 1 - v1 <= v2
            if a1 == a2:
                return
            v1 = a1 + (a2 - a1) // 2
            v2 = points[order[v1]][0]
            merge_sort(a1, v1)
            merge_sort(v1 + 1, a2)
            v3, v4, v5 = ([], [], [])
            v6, v7 = (a1, v1 + 1)
            while v6 <= v1 or v7 <= a2:
                if v7 == a2 + 1 or (v6 <= v1 and points[order[v6]][1] <= points[order[v7]][1]):
                    update(v5, order[v6])
                    if v2 - points[order[v6]][0] <= result[0]:
                        v4.append(order[v6])
                    v3.append(order[v6])
                    v6 += 1
                else:
                    update(v4, order[v7])
                    if points[order[v7]][0] - v2 <= result[0]:
                        v5.append(order[v7])
                    v3.append(order[v7])
                    v7 += 1
            order[a1:a2 + 1] = v3
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
