class C1(object):

    def getWordsInLongestSubsequence(self, a1, a2, a3):
        """
        """
        return [a2[i] for v1 in range(a1) if v1 == 0 or a3[v1 - 1] != a3[v1]]
