class C1(object):

    def getSmallestString(self, a1, a2):
        """
        """
        v1 = ord('z') - ord('a')
        a2 -= a1
        v3 = ['a'] * a1
        for v4 in reversed(range(a1)):
            v5 = min(a2, v1)
            v3[v4] = chr(ord('a') + v5)
            a2 -= v5
            if a2 == 0:
                break
        return ''.join(v3)
