class C1(object):

    def checkSubarraySum(self, a1, a2):
        """
        """
        v1 = 0
        v2 = {0: -1}
        for v3, v4 in enumerate(a1):
            v1 += v4
            if a2:
                v1 %= a2
            if v1 in v2:
                if v3 - v2[v1] > 1:
                    return True
            else:
                v2[v1] = v3
        return False
