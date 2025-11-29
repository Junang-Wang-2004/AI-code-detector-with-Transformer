class C1(object):

    def canMakeArithmeticProgression(self, a1):
        """
        """
        v1 = min(a1)
        v2 = (max(a1) - v1) // (len(a1) - 1)
        if not v2:
            return True
        v3 = 0
        while v3 < len(a1):
            if a1[v3] == v1 + v3 * v2:
                v3 += 1
            else:
                v4, v5 = divmod(a1[v3] - v1, v2)
                if v5 or v4 >= len(a1) or a1[v3] == a1[v4]:
                    return False
                a1[v3], a1[v4] = (a1[v4], a1[v3])
        return True
