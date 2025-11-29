import collections

class C1(object):

    def minStickers(self, a1, a2):
        """
        """

        def minStickersHelper(a1, a2, a3):
            if ''.join(a2) in a3:
                return a3[''.join(a2)]
            v1 = collections.Counter(a2)
            v2 = float('inf')
            for v3 in a1:
                if v3[a2[0]] == 0:
                    continue
                v4 = []
                for v5 in list(v1.keys()):
                    if v1[v5] > v3[v5]:
                        v4 += [v5] * (v1[v5] - v3[v5])
                if len(v4) != len(a2):
                    v6 = minStickersHelper(a1, v4, a3)
                    if v6 != -1:
                        v2 = min(v2, 1 + v6)
            a3[''.join(a2)] = -1 if v2 == float('inf') else v2
            return a3[''.join(a2)]
        v1 = list(map(collections.Counter, a1))
        v2 = {'': 0}
        return minStickersHelper(v1, a2, v2)
