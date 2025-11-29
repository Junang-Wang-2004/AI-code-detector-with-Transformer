import collections
import sortedcontainers

class C1(object):

    def minimumIncompatibility(self, a1, a2):
        """
        """

        def greedy(a1, a2, a3):
            v1 = collections.Counter(a1)
            if max(v1.values()) > a2:
                return -1
            v2 = sortedcontainers.SortedList(iter(v1.keys()))
            v3 = collections.defaultdict(collections.OrderedDict)
            for v4 in v2:
                v3[v1[v4]][v4] = v1[v4]
            v5 = [[] for v6 in range(a2)]
            v7 = 0
            while v2:
                if len(v5) - v7 in v3:
                    for v4 in v3[len(v5) - v7].keys():
                        for v8 in range(v7, len(v5)):
                            v5[v8].append(v4)
                        v1.pop(v4)
                        v2.remove(v4)
                    v3.pop(len(v5) - v7)
                v9 = []
                v10 = (lambda x: v4) if not a3 else reversed
                for v4 in v10(v2):
                    v5[v7].append(v4)
                    v3[v1[v4]].pop(v4)
                    if not v3[v1[v4]]:
                        v3.pop(v1[v4])
                    v1[v4] -= 1
                    if not v1[v4]:
                        v1.pop(v4)
                        v9.append(v4)
                    else:
                        v3[v1[v4]][v4] = v1[v4]
                    if len(v5[v7]) == len(a1) // a2:
                        v7 += 1
                        break
                for v4 in v9:
                    v2.remove(v4)
            return sum([max(stk) - min(stk) for v11 in v5])
        return min(greedy(a1, a2, False), greedy(a1, a2, True))
