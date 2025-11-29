# Time:  O(nlogn)
# Space: O(1)
# brute force
class Solution2(object):
    def countEven(self, num):
        """
        """
        def parity(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result%2

        return sum(parity(x) == 0 for x in range(1, num+1))


