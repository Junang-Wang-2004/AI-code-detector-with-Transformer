import collections

class C1(object):

    def findLength(self, a1, a2):
        """
        """
        if len(a1) < len(a2):
            return self.findLength(a2, a1)
        v1 = 0
        v2 = [[0] * (len(a2) + 1) for v3 in range(2)]
        for v4 in range(len(a1)):
            for v5 in range(len(a2)):
                if a1[v4] == a2[v5]:
                    v2[(v4 + 1) % 2][v5 + 1] = v2[v4 % 2][v5] + 1
                else:
                    v2[(v4 + 1) % 2][v5 + 1] = 0
            v1 = max(v1, max(v2[(v4 + 1) % 2]))
        return v1
