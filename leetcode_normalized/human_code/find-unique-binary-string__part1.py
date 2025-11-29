class C1(object):

    def findDifferentBinaryString(self, a1):
        """
        """
        return ''.join(('01'[a1[i][i] == '0'] for v1 in range(len(a1))))
