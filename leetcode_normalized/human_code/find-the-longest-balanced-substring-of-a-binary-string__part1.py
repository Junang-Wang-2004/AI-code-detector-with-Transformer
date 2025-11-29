class C1(object):

    def findTheLongestBalancedSubstring(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3, v4 = (v2 + 1, v2)
            while v3 - 1 >= 0 and v4 + 1 < len(a1) and (a1[v3 - 1] == '0') and (a1[v4 + 1] == '1'):
                v3 -= 1
                v4 += 1
            v1 = max(v1, v4 - v3 + 1)
        return v1
