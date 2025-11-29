import collections
import itertools

class C1(object):

    def alertNames(self, a1, a2):
        """
        """
        v1 = 3
        v2 = collections.defaultdict(list)
        for v3, v4 in zip(a1, a2):
            v5, v6 = list(map(int, v4.split(':')))
            v2[v3].append(v5 * 60 + v6)
        v7 = []
        for v3, v8 in v2.items():
            v8.sort()
            v9 = 0
            for v10, v11 in enumerate(v8):
                while v11 - v8[v9] > 60:
                    v9 += 1
                if v10 - v9 + 1 >= v1:
                    v7.append(v3)
                    break
        v7.sort()
        return v7
