class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = a1.count('0')
        for v2 in range(len(a1) + 1):
            if v2 * a2 - v1 & 1:
                continue
            if v2 & 1:
                if v1 <= v2 * a2 <= v1 * v2 + (len(a1) - v1) * (v2 - 1):
                    return v2
            elif v1 <= v2 * a2 <= v1 * (v2 - 1) + (len(a1) - v1) * v2:
                return v2
        return -1
