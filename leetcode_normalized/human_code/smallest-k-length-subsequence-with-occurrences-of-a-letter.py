class C1(object):

    def smallestSubsequence(self, a1, a2, a3, a4):
        """
        """
        v1 = []
        v2 = [0] * (len(a1) + 1)
        for v3 in reversed(range(len(v2) - 1)):
            v2[v3] = v2[v3 + 1] + (a1[v3] == a3)
        for v3, v4 in enumerate(a1):
            while v1 and v1[-1] > v4 and (len(v1) + (len(a1) - v3) > a2) and (v1[-1] != a3 or a4 + 1 <= v2[v3]):
                a4 += v1.pop() == a3
            if len(v1) < min(a2 - (a4 - (v4 == a3)), a2):
                a4 -= v4 == a3
                v1.append(v4)
        return ''.join(v1)
