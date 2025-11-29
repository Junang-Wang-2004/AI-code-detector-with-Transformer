class C1(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = [0] * 10
        for v2 in reversed(range(len(a1))):
            if a1[v2] in '05' and v1[0] or (a1[v2] in '27' and v1[5]):
                return len(a1) - v2 - 2
            v1[ord(a1[v2]) - ord('0')] = 1
        return len(a1) - v1[0]
