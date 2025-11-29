class C1(object):

    def splitLoopedString(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            v1 += max(v2, v2[::-1])
        v2 = ''.join(v1)
        v3, v4 = ('a', 0)
        for v5 in range(len(a1)):
            v6 = ''.join([v2[v4 + len(a1[v5]):], v2[0:v4]])
            for v7 in (a1[v5], a1[v5][::-1]):
                for v8 in range(len(a1[v5])):
                    if v7[v8] >= v3[0]:
                        v3 = max(v3, ''.join([v7[v8:], v6, v7[:v8]]))
            v4 += len(a1[v5])
        return v3
