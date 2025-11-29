class C1(object):

    def repeatedSubstringPattern(self, a1):
        v1 = len(a1)
        for v2 in range(1, v1 // 2 + 1):
            if v1 % v2 == 0:
                v3 = a1[:v2]
                if v3 * (v1 // v2) == a1:
                    return True
        return False
