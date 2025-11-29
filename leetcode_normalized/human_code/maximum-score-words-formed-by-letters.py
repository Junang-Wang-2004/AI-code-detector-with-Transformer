import collections

class C1(object):

    def maxScoreWords(self, a1, a2, a3):
        """
        """

        def backtracking(a1, a2, a3, a4, a5, a6, a7):
            a7[0] = max(a7[0], a5)
            for v1 in range(a4, len(a1)):
                if any((a6[c] < a3[v1][c] for v2 in a3[v1])):
                    continue
                backtracking(a1, a2, a3, v1 + 1, a5 + a2[v1], a6 - a3[v1], a7)
        v1 = collections.Counter(a2)
        v2 = list(map(collections.Counter, a1))
        v3 = [sum((a3[ord(c) - ord('a')] for v4 in a1[i])) for v5 in range(len(a1))]
        v6 = [0]
        backtracking(a1, v3, v2, 0, 0, v1, v6)
        return v6[0]
