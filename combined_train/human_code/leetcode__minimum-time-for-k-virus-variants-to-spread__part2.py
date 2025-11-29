import collections

class C1(object):

    def minDayskVariants(self, a1, a2):
        """
        """

        def add_rec(a1, a2):
            v1, v2, v3, v4 = a1
            a2[v1][v2] += 1
            a2[v1][v4 + 1] -= 1
            a2[v3 + 1][v2] -= 1
            a2[v3 + 1][v4 + 1] += 1

        def check(a1, a2, a3):
            v1 = collections.defaultdict(lambda: collections.defaultdict(int))
            v2 = set()
            for v3, v4 in a1:
                add_rec([v3 - a3, v4 - a3, v3 + a3, v4 + a3], v1)
                v2.add(v4 - a3)
                v2.add(v4 + a3 + 1)
            v5 = sorted(v2)
            v6 = sorted(v1.keys())
            v7 = collections.Counter()
            for v3 in v6:
                for v4, v8 in v1[v3].items():
                    v7[v4] += v8
                v9 = 0
                for v4 in v5:
                    v9 += v7[v4]
                    if v9 >= a2:
                        return True
            return False
        a1 = [[x + y, x - y] for v2, v3 in a1]
        v4 = min(a1)[0]
        v5 = max(a1)[0]
        v6 = min(a1, key=lambda x: v2[1])[1]
        v7 = max(a1, key=lambda x: v2[1])[1]
        v8, v9 = (0, (v5 - v4 + (v7 - v6) + 1) // 2)
        while v8 <= v9:
            v10 = v8 + (v9 - v8) // 2
            if check(a1, a2, v10):
                v9 = v10 - 1
            else:
                v8 = v10 + 1
        return v8
