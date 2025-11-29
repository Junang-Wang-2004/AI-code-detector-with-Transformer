# Time:  O(l * nlogn)
# Space: O(n * l)

import itertools


# hash table, sort
class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        """
        LOOKUP = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        sorted_codes = []
        for c, b, a in zip(code, businessLine, isActive):
            if a and c and b in LOOKUP and all(x.isalnum() or x == '_' for x in c):
                sorted_codes.append((LOOKUP[b], c))
        sorted_codes.sort()
        return [c for _, c in sorted_codes]
