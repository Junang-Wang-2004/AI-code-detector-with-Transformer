import collections

class C1(object):

    def findMinStep(self, a1, a2):
        """
        """

        def shrink(a1):
            v1 = []
            v2 = 0
            for v3 in range(len(a1) + 1):
                if v3 == len(a1) or a1[v3] != a1[v2]:
                    if v1 and v1[-1][0] == a1[v2]:
                        v1[-1][1] += v3 - v2
                        if v1[-1][1] >= 3:
                            v1.pop()
                    elif a1 and v3 - v2 < 3:
                        v1 += ([a1[v2], v3 - v2],)
                    v2 = v3
            v4 = []
            for v5 in v1:
                v4 += [v5[0]] * v5[1]
            return v4

        def findMinStepHelper2(a1, a2, a3):
            v1 = float('inf')
            for v2 in range(len(a2)):
                for v3 in range(len(a1) + 1):
                    v4 = shrink(a1[0:v3] + a2[v2:v2 + 1] + a1[v3:])
                    v5 = a2[0:v2] + a2[v2 + 1:]
                    v1 = min(v1, findMinStepHelper(v4, v5, a3) + 1)
            return v1

        def find(a1, a2, a3):
            for v1 in range(a3, len(a1)):
                if a1[v1] == a2:
                    return v1
            return -1

        def findMinStepHelper(a1, a2, a3):
            if not a1:
                return 0
            if not a2:
                return float('inf')
            if tuple(a2) in a3[tuple(a1)]:
                return a3[tuple(a1)][tuple(a2)]
            v1 = float('inf')
            for v2 in range(len(a2)):
                v3 = 0
                while v3 < len(a1):
                    v4 = find(a1, a2[v2], v3)
                    if v4 == -1:
                        break
                    if v4 < len(a1) - 1 and a1[v4] == a1[v4 + 1]:
                        v5 = shrink(a1[0:v4] + a1[v4 + 2:])
                        v6 = a2[0:v2] + a2[v2 + 1:]
                        v1 = min(v1, findMinStepHelper(v5, v6, a3) + 1)
                        v4 += 1
                    elif v2 > 0 and a2[v2] == a2[v2 - 1]:
                        v5 = shrink(a1[0:v4] + a1[v4 + 1:])
                        v6 = a2[0:v2 - 1] + a2[v2 + 1:]
                        v1 = min(v1, findMinStepHelper(v5, v6, a3) + 2)
                    v3 = v4 + 1
            a3[tuple(a1)][tuple(a2)] = v1
            return v1
        a1, a2 = (list(a1), list(a2))
        a2.sort()
        v3 = findMinStepHelper(a1, a2, collections.defaultdict(dict))
        if v3 == float('inf'):
            v3 = findMinStepHelper2(a1, a2, collections.defaultdict(dict))
        return -1 if v3 == float('inf') else v3
