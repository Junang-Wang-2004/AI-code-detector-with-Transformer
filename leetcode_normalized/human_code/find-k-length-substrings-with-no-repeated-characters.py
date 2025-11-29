class C1(object):

    def numKLenSubstrNoRepeats(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        v3 = set()
        for v4 in range(len(a1)):
            while a1[v4] in v3:
                v3.remove(a1[v2])
                v2 += 1
            v3.add(a1[v4])
            v1 += v4 - v2 + 1 >= a2
        return v1
