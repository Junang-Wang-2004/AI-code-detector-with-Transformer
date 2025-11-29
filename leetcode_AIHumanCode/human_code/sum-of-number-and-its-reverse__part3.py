# Time:  O(nlogn)
# Space: O(logn)
# brute force
class Solution3(object):
    def sumOfNumberAndReverse(self, num):
        """
        """
        return any(x+int(str(x)[::-1]) == num for x in range(num//2, num+1))
