class C1(object):

    def largestSubarray(self, a1, a2):
        """
        """
        v1, v2, v3 = (0, 1, 0)
        while v2 + a2 - 1 < len(a1) and v2 + v3 < len(a1):
            if a1[v1 + v3] == a1[v2 + v3]:
                v3 += 1
                continue
            if a1[v1 + v3] > a1[v2 + v3]:
                v2 += v3 + 1
            else:
                v1 = max(v2, min(v1 + v3 + 1, len(a1) - a2))
                v2 = v1 + 1
            v3 = 0
        return a1[v1:v1 + a2]
