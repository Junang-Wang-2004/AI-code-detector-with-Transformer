from functools import reduce

class C1(object):

    def minimumSubarrayLength(self, a1, a2):
        """
        """
        v1 = float('inf')
        for v2 in range(len(a1)):
            v3 = 0
            for v4 in range(v2, len(a1)):
                v3 |= a1[v4]
                if v3 < a2:
                    continue
                v1 = min(v1, v4 - v2 + 1)
                break
        return v1 if v1 != float('inf') else -1
