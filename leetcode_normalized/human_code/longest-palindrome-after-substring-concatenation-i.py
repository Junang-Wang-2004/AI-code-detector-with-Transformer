class C1(object):

    def longestPalindrome(self, a1, a2):
        """
        """

        def manacher(a1):
            a1 = '^#' + '#'.join(a1) + '#$'
            v2 = [0] * len(a1)
            v3, v4 = (0, 0)
            for v5 in range(1, len(a1) - 1):
                v6 = 2 * v3 - v5
                if v4 > v5:
                    v2[v5] = min(v4 - v5, v2[v6])
                while a1[v5 + 1 + v2[v5]] == a1[v5 - 1 - v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2

        def longest_palindrome(a1):
            v1 = [0] * (len(a1) + 1)
            v2 = manacher(a1)
            for v3 in range(1, len(v2) - 1):
                v1[(v3 - v2[v3]) // 2] = v2[v3]
            return v1
        a2 = a2[::-1]
        v2 = longest_palindrome(a1)
        v3 = longest_palindrome(a2)
        v4 = 0
        v5 = [[0] * (len(a2) + 1) for v6 in range(len(a1) + 1)]
        for v7 in range(len(a1)):
            for v8 in range(len(a2)):
                v5[v7 + 1][v8 + 1] = v5[v7][v8] + 2 if a1[v7] == a2[v8] else 0
                v4 = max(v4, v5[v7 + 1][v8 + 1] + max(v2[v7 + int(a1[v7] == a2[v8])], v3[v8 + int(a1[v7] == a2[v8])]))
        return v4
