import random

class C1(object):

    def highestRankedKItems(self, a1, a2, a3, a4):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def nth_element(a1, a2, a3=0, a4=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1 = len(a1) - 1
            while a3 <= v1:
                v2 = random.randint(a3, v1)
                v3, v4 = tri_partition(a1, a3, v1, a1[v2], a4)
                if v3 <= a2 <= v4:
                    return
                elif v3 > a2:
                    v1 = v3 - 1
                else:
                    a3 = v4 + 1

        def get_val(a1):
            return (lookup[a1[0]][a1[1]], a1[a1[0]][a1[1]], a1[0], a1[1])
        v2 = []
        v3 = [a3]
        v4 = [[-1] * len(a1[0]) for v5 in range(len(a1))]
        v6 = v4[a3[0]][a3[1]] = 0
        while v3:
            if len(v2) >= a4:
                if len(v2) > a4:
                    nth_element(v2, a4 - 1, compare=lambda a, b: get_val(a) < get_val(b))
                    v2 = v2[:a4]
                break
            v7 = []
            for v8, v9 in v3:
                if a2[0] <= a1[v8][v9] <= a2[1]:
                    v2.append([v8, v9])
                for v10, v11 in v1:
                    v12, v13 = (v8 + v10, v9 + v11)
                    if not (0 <= v12 < len(a1) and 0 <= v13 < len(a1[0]) and a1[v12][v13] and (v4[v12][v13] == -1)):
                        continue
                    v4[v12][v13] = v6 + 1
                    v7.append((v12, v13))
            v3 = v7
            v6 += 1
        v2.sort(key=lambda x: get_val(x))
        return v2
