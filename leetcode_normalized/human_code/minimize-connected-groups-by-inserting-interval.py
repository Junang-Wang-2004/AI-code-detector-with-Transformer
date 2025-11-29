class C1(object):

    def minConnectedGroups(self, a1, a2):
        """
        """
        a1.sort()
        v1 = 0
        v2 = [0] * (len(a1) + 1)
        v3 = float('-inf')
        v4 = 0
        for v5 in range(len(a1)):
            v2[v5 + 1] = v2[v5] + int(v3 < a1[v5][0])
            v3 = max(v3, a1[v5][1])
            while a1[v5][0] - a1[v4][1] > a2:
                v4 += 1
            v1 = max(v1, v2[v5 + 1] - v2[v4 + 1])
        return v2[-1] - v1
