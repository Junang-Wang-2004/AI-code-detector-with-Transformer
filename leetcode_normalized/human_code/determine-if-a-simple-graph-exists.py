class C1(object):

    def simpleGraphExists(self, a1):
        """
        """
        if sum(a1) % 2:
            return False
        a1.sort(reverse=True)
        v1 = 0
        v2 = sum(a1)
        v3 = 0
        v4 = len(a1) - 1
        for v5 in range(1, len(a1) + 1):
            v1 += a1[v5 - 1]
            v2 -= a1[v5 - 1]
            while v4 >= 0 and a1[v4] < v5:
                v3 += a1[v4]
                v4 -= 1
            if not v1 <= v5 * (v5 - 1) + ((v4 - v5 + 1) * v5 + v3 if v4 - v5 + 1 > 0 else v2):
                return False
        return True
