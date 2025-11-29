class C1(object):

    def maxFreqSum(self, a1):
        """
        """
        v1 = {'a', 'e', 'i', 'o', 'u'}
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        return max((v2[i] for v4 in range(26) if chr(v4 + ord('a')) in v1)) + max((v2[v4] for v4 in range(26) if chr(v4 + ord('a')) not in v1))
