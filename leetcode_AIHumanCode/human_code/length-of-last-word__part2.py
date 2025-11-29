# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])

