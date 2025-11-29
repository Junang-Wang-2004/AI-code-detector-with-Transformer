# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isIdealPermutation(self, A):
        """
        """
        return all(abs(v-i) <= 1 for i,v in enumerate(A))


