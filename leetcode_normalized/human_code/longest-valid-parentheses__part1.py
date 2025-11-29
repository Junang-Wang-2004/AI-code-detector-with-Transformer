class C1(object):

    def longestValidParentheses(self, a1):
        """
        """

        def length(a1, a2, a3):
            v1, v2 = (0, 0)
            for v3 in a1:
                if a1[v3] == a3:
                    v1 += 1
                else:
                    v1 -= 1
                    if v1 < 0:
                        a2, v1 = (v3, 0)
                    elif v1 == 0:
                        v2 = max(v2, abs(v3 - a2))
            return v2
        return max(length(range(len(a1)), -1, '('), length(reversed(range(len(a1))), len(a1), ')'))
