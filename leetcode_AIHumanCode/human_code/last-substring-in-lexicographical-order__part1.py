# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lastSubstring(self, s):
        """
        """
        left, right, l = 0, 1, 0
        while right+l < len(s):
            if s[left+l] == s[right+l]:
                l += 1
                continue
            if s[left+l] > s[right+l]:
                right += l+1
            else:
                left = max(right, left+l+1)
                right = left+1
            l = 0
        return s[left:]


