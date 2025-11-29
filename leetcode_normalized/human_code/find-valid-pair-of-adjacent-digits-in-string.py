class C1(object):

    def findValidPair(self, a1):
        """
        """
        v1 = [0] * 9
        for v2 in a1:
            v1[ord(v2) - ord('1')] += 1
        for v3 in range(len(a1) - 1):
            if a1[v3] != a1[v3 + 1] and v1[ord(a1[v3]) - ord('1')] == ord(a1[v3]) - ord('0') and (v1[ord(a1[v3 + 1]) - ord('1')] == ord(a1[v3 + 1]) - ord('0')):
                return a1[v3:v3 + 2]
        return ''
