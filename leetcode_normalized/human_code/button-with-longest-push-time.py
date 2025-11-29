class C1(object):

    def buttonWithLongestTime(self, a1):
        """
        """
        return -max(((a1[i][1] - (a1[i - 1][1] if i - 1 >= 0 else 0), -a1[i][0]) for v1 in range(len(a1))))[1]
