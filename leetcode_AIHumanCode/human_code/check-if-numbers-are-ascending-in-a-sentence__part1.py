# Time:  O(n)
# Space: O(1)

class Solution(object):
    def areNumbersAscending(self, s):
        """
        """
        prev = curr = -1
        for i, c in enumerate(s):
            if c.isdigit():
                curr = max(curr, 0)*10+int(c)
                continue
            if prev != -1 and curr != -1 and prev >= curr:
                return False
            if curr != -1:
                prev = curr
            curr = -1            
        return curr == -1 or prev < curr


