import collections

class C1(object):

    def validArrangement(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = collections.defaultdict(int)
        for v3, v4 in a1:
            v1[v3].append(v4)
            v2[v3] += 1
            v2[v4] -= 1
        v5 = []
        v6 = [next((v3 for v3, v7 in v2.items() if v7 == 1), next(iter(v2.keys())))]
        while v6:
            while v1[v6[-1]]:
                v6.append(v1[v6[-1]].pop())
            v5.append(v6.pop())
        v5.reverse()
        return [[v5[i], v5[i + 1]] for v8 in range(len(v5) - 1)]
