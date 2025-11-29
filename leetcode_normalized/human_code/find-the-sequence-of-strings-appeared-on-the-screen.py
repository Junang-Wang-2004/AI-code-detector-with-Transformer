class C1(object):

    def stringSequence(self, a1):
        """
        """
        return [a1[:i] + chr(x) for v1 in range(len(a1)) for v2 in range(ord('a'), ord(a1[v1]) + 1)]
