# Time:  O(logn)
# Space: O(1)

# greedy, trick
# reference: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203994/java-c-python-1-line-solution/
class Solution(object):
    def minOperations(self, n):
        """
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        return popcount(n^(n*0b11))


