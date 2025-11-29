# Time:  O(n)
# Space: O(1)
# sliding window
class Solution2(object):
    def numberOfAlternatingGroups(self, colors):
        """
        """
        return sum(colors[i] != colors[(i+1)%len(colors)] != colors[(i+2)%len(colors)] for i in range(len(colors)))
