# Time:  O(n * l)
# Space: O(1)

# array
class Solution(object):
    def maxDistance(self, words):
        """
        """
        for i in range(len(words)//2+1):
            if words[~i] != words[0] or words[i] != words[-1]:
                return len(words)-i
        return 0
