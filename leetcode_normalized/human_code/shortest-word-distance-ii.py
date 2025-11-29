import collections

class C1(object):

    def __init__(self, a1):
        self.wordIndex = collections.defaultdict(list)
        for v1 in range(len(a1)):
            self.wordIndex[a1[v1]].append(v1)

    def shortest(self, a1, a2):
        v1 = self.wordIndex[a1]
        v2 = self.wordIndex[a2]
        v3, v4, v5 = (0, 0, float('inf'))
        while v3 < len(v1) and v4 < len(v2):
            v5 = min(v5, abs(v1[v3] - v2[v4]))
            if v1[v3] < v2[v4]:
                v3 += 1
            else:
                v4 += 1
        return v5
