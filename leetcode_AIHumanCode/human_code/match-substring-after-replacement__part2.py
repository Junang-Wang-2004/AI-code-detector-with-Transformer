# Time:  O(n * k), n = len(s), k = len(sub)
# Space: O(m), m = len(mappings)
import collections


# brute force
class Solution2(object):
    def matchReplacement(self, s, sub, mappings):
        """
        """
        def check(i):
            return all(sub[j] == s[i+j] or (sub[j], s[i+j]) in lookup for j in range(len(sub)))
            
        lookup = set()
        for a, b in mappings:
            lookup.add((a, b))
        return any(check(i) for i in range(len(s)-len(sub)+1))
