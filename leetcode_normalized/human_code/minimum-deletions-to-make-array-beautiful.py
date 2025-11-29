class C1(object):

    def minDeletion(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1) - 1):
            v1 += int(v2 % 2 == v1 % 2 and a1[v2] == a1[v2 + 1])
        return v1 + (len(a1) - v1) % 2
