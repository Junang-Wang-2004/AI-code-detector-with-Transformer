# Time:  O(n)
# Space: O(1)

  # Generator version of zip.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for p, w in zip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True


