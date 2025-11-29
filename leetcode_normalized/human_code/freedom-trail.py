import collections

class C1(object):

    def findRotateSteps(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in range(len(a1)):
            v1[a1[v2]].append(v2)
        v3 = [[0] * len(a1) for v4 in range(2)]
        v5 = [0]
        for v2 in range(1, len(a2) + 1):
            v3[v2 % 2] = [float('inf')] * len(a1)
            for v6 in v1[a2[v2 - 1]]:
                for v7 in v5:
                    v3[v2 % 2][v6] = min(v3[v2 % 2][v6], min((v7 + len(a1) - v6) % len(a1), (v6 + len(a1) - v7) % len(a1)) + v3[(v2 - 1) % 2][v7])
            v5 = v1[a2[v2 - 1]]
        return min(v3[len(a2) % 2]) + len(a2)
