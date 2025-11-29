# Time:  O(nlogn)
# Space: O(logn)
# brute force
class Solution3(object):
    def countEven(self, num):
        """
        """
        return sum(sum(map(int, str(x)))%2 == 0 for x in range(1, num+1))
