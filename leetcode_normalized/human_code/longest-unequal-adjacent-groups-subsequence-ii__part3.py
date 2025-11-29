import itertools

class C1(object):

    def getWordsInLongestSubsequence(self, a1, a2, a3):
        """
        """

        def check(a1, a2):
            return len(a1) == len(a2) and sum((a != b for v1, v2 in zip(a1, a2))) == 1
        v1 = [[] for v2 in range(a1)]
        for v3 in range(a1):
            for v4 in range(v3):
                if a3[v3] != a3[v4] and check(a2[v4], a2[v3]) and (len(v1[v4]) > len(v1[v3])):
                    v1[v3] = v1[v4]
            v1[v3] = v1[v3] + [v3]
        return [a2[x] for v5 in max(v1, key=lambda x: len(v5))]
