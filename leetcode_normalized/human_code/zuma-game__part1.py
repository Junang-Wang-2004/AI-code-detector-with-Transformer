import collections

class C1(object):

    def findMinStep(self, a1, a2):
        """
        """

        def shrink(a1):
            while True:
                v1 = 0
                for v2 in range(len(a1)):
                    while v1 < len(a1) and a1[v2] == a1[v1]:
                        v1 += 1
                    if v1 - v2 >= 3:
                        a1 = a1[0:v2] + a1[v1:]
                        break
                else:
                    break
            return a1

        def findMinStepHelper(a1, a2, a3):
            if not a1:
                return 0
            if not a2:
                return float('inf')
            if tuple(a2) in a3[tuple(a1)]:
                return a3[tuple(a1)][tuple(a2)]
            v1 = float('inf')
            for v2 in range(len(a2)):
                for v3 in range(len(a1) + 1):
                    v4 = shrink(a1[0:v3] + a2[v2:v2 + 1] + a1[v3:])
                    v5 = a2[0:v2] + a2[v2 + 1:]
                    v1 = min(v1, findMinStepHelper(v4, v5, a3) + 1)
            a3[tuple(a1)][tuple(a2)] = v1
            return v1
        v1 = collections.defaultdict(dict)
        a1, a2 = (list(a1), list(a2))
        v4 = findMinStepHelper(a1, a2, v1)
        return -1 if v4 == float('inf') else v4
