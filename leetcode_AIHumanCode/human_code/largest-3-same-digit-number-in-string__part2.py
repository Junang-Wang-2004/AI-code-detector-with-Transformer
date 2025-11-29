# Time:  O(n)
# Space: O(1)
# string
class Solution2(object):
    def largestGoodInteger(self, num):
        """
        """
        return max(num[i] if num[i] == num[i+1] == num[i+2] else '' for i in range(len(num)-2))*3
