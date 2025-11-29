class C1(object):

    def checkSubarraySum(self, a1, a2):
        v1 = {0: -1}
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v2 += a1[v3]
            if a2 != 0:
                v2 %= a2
            if v2 in v1:
                if v3 - v1[v2] > 1:
                    return True
            else:
                v1[v2] = v3
            v3 += 1
        return False
