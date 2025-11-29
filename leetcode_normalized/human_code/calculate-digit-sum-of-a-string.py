class C1(object):

    def digitSum(self, a1, a2):
        """
        """
        while len(a1) > a2:
            a1 = ''.join(map(str, (sum(map(int, a1[i:i + a2])) for v2 in range(0, len(a1), a2))))
        return a1
