class C1(object):

    def alphabetBoardPath(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = []
        for v4 in a1:
            v5, v6 = divmod(ord(v4) - ord('a'), 5)
            v3.append('U' * max(v2 - v5, 0))
            v3.append('L' * max(v1 - v6, 0))
            v3.append('R' * max(v6 - v1, 0))
            v3.append('D' * max(v5 - v2, 0))
            v3.append('!')
            v1, v2 = (v6, v5)
        return ''.join(v3)
