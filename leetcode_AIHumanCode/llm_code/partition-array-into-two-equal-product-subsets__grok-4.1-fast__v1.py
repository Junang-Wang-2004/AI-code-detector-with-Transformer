class Solution:
    def checkEqualPartitions(self, s, t):
        prod_all = 1
        sq = t * t
        for val in s:
            prod_all *= val
            if prod_all > sq:
                return False
        if prod_all != sq:
            return False
        sz = len(s)
        max_mask = 1 << sz
        for k in range(1, max_mask - 1):
            partial = 1
            for j in range(sz):
                if (k & (1 << j)) != 0:
                    partial *= s[j]
                    if partial > t:
                        break
            else:
                if partial == t:
                    return True
        return False
