import collections

class C1(object):

    def executeInstructions(self, a1, a2, a3):
        v1 = {'U': -1, 'R': 0, 'D': 1, 'L': 0}
        v2 = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
        v3, v4 = a2
        v5 = len(a3)
        v6 = [v1[ch] for v7 in a3]
        v8 = [v2[v7] for v7 in a3]
        v9 = self._get_limits(a1, v3, v6)
        v10 = self._get_limits(a1, v4, v8)
        return [min(v9[i], v10[i]) for v11 in range(v5)]

    def _get_limits(self, a1, a2, a3):
        v1 = len(a3)
        v2 = list(range(v1, 0, -1))
        v3 = collections.defaultdict(list)
        v4 = 0
        v3[a2 - v4].append(0)
        for v5 in range(v1):
            v4 += a3[v5]
            for v6 in (a1 - v4, -v4 - 1):
                if v6 in v3:
                    for v7 in v3[v6]:
                        v2[v7] = min(v2[v7], v5 - v7)
                    v3[v6] = []
            v3[a2 - v4].append(v5 + 1)
        return v2
