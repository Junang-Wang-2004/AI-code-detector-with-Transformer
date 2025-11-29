import collections

class C1(object):

    def minimumIncompatibility(self, a1, a2):
        """
        """

        def greedy(a1, a2, a3):
            v1 = collections.Counter(a1)
            if max(v1.values()) > a2:
                return -1
            v2 = sorted(list(v1.keys()), reverse=a3)
            v3 = [[] for v4 in range(a2)]
            v5, v6 = (0, len(a1))
            while v6:
                for v7 in v2:
                    if v1[v7] != len(v3) - v5:
                        continue
                    for v8 in range(v5, len(v3)):
                        v3[v8].append(v7)
                    v6 -= v1[v7]
                    v1[v7] = 0
                for v7 in v2:
                    if not v1[v7]:
                        continue
                    v3[v5].append(v7)
                    v6 -= 1
                    v1[v7] -= 1
                    if len(v3[v5]) == len(a1) // a2:
                        v5 += 1
                        break
            return sum([max(stk) - min(stk) for v9 in v3])
        return min(greedy(a1, a2, False), greedy(a1, a2, True))
