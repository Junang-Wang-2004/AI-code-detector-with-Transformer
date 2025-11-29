class C1(object):

    def bagOfTokensScore(self, a1, a2):
        """
        """
        a1.sort()
        v1, v2 = (0, 0)
        v3, v4 = (0, len(a1) - 1)
        while v3 <= v4:
            if a2 >= a1[v3]:
                a2 -= a1[v3]
                v3 += 1
                v2 += 1
                v1 = max(v1, v2)
            elif v2 > 0:
                v2 -= 1
                a2 += a1[v4]
                v4 -= 1
            else:
                break
        return v1
