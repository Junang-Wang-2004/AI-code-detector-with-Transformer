class C1(object):

    def repeatedNTimes(self, a1):
        """
        """
        for v1 in range(2, len(a1)):
            if a1[v1 - 1] == a1[v1] or a1[v1 - 2] == a1[v1]:
                return a1[v1]
        return a1[0]
