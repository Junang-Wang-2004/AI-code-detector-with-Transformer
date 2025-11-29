class C1(object):

    def minSwaps(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 == ']':
                v2 += 1
                v1 = max(v1, v2)
            else:
                v2 -= 1
        return (v1 + 1) // 2
