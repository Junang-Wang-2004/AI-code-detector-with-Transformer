class C1(object):

    def maxPalindromes(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3 in range(2 * len(a1) - 1):
            v4, v5 = (v3 // 2, v3 // 2 + v3 % 2)
            while v4 >= v2 and v5 < len(a1) and (a1[v4] == a1[v5]):
                if v5 - v4 + 1 >= a2:
                    v2 = v5 + 1
                    v1 += 1
                    break
                v4, v5 = (v4 - 1, v5 + 1)
        return v1
