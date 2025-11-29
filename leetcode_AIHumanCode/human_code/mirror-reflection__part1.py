# Time:  O(1)
# Space: O(1)

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        """
        # explanation commented in the following solution
        return 2 if (p & -p) > (q & -q) else 0 if (p & -p) < (q & -q) else 1


