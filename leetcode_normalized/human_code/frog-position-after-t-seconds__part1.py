import collections

class C1(object):

    def frogPosition(self, a1, a2, a3, a4):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [(a3, 1, 0, 1)]
        while v4:
            v5 = []
            while v4:
                a3, v7, v8, v9 = v4.pop()
                if not a3 or not len(v1[v7]) - (v8 != 0):
                    if v7 == a4:
                        return 1.0 / v9
                    continue
                for v10 in v1[v7]:
                    if v10 == v8:
                        continue
                    v5.append((a3 - 1, v10, v7, v9 * (len(v1[v7]) - (v8 != 0))))
            v4 = v5
        return 0.0
