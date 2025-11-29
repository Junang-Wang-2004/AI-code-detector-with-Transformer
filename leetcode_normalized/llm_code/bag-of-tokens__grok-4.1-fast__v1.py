class C1:

    def bagOfTokensScore(self, a1, a2):
        a1.sort()
        v1 = 0
        v2 = 0
        while a1:
            if a2 >= a1[0]:
                a2 -= a1.pop(0)
                v2 += 1
                v1 = max(v1, v2)
            elif v2 > 0:
                v2 -= 1
                a2 += a1.pop()
            else:
                break
        return v1
