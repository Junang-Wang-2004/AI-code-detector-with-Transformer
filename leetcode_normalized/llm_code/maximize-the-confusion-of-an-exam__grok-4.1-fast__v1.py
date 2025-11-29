class C1(object):

    def maxConsecutiveAnswers(self, a1, a2):

        def window_majority(a1):
            v1 = 0
            v2 = 0
            v3 = 0
            for v4 in range(len(a1)):
                if a1[v4] != a1:
                    v1 += 1
                while v1 > a2 and v2 <= v4:
                    if a1[v2] != a1:
                        v1 -= 1
                    v2 += 1
                v3 = max(v3, v4 - v2 + 1)
            return v3
        return max(window_majority('T'), window_majority('F'))
