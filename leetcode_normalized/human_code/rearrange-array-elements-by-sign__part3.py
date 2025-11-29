class C1(object):

    def rearrangeArray(self, a1):
        """
        """
        v1, v2 = ([], [])
        for v3 in reversed(range(len(a1))):
            if a1[v3] > 0:
                v1.append(a1[v3])
            else:
                v2.append(a1[v3])
        v4 = []
        for v3 in range(len(a1)):
            if v3 % 2 == 0:
                v4.append(v1.pop())
            else:
                v4.append(v2.pop())
        return v4
