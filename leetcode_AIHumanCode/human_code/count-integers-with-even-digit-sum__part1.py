# Time:  O(logn)
# Space: O(1)

# math
class Solution(object):
    def countEven(self, num):
        """
        """
        def parity(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result%2

        return (num-parity(num))//2


