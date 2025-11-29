import collections

class C1(object):

    def sequenceReconstruction(self, a1, a2):
        """
        """
        if not a2:
            return False
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[a1[v2]] = v2
        v3 = [False] * (len(a1) + 1)
        v4 = len(a1) - 1
        for v5 in a2:
            for v2 in range(len(v5)):
                if not 0 < v5[v2] <= len(a1):
                    return False
                if v2 == 0:
                    continue
                if v1[v5[v2 - 1]] >= v1[v5[v2]]:
                    return False
                if v3[v5[v2 - 1]] == False and v1[v5[v2 - 1]] + 1 == v1[v5[v2]]:
                    v3[v5[v2 - 1]] = True
                    v4 -= 1
        return v4 == 0
