# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


