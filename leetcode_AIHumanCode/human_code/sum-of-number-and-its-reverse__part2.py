# Time:  O(nlogn)
# Space: O(1)
# brute force
class Solution2(object):
    def sumOfNumberAndReverse(self, num):
        """
        """
        def reverse(n):
            result = 0
            while n:
                result = result*10 + n%10
                n //= 10            
            return result

        return any(x+reverse(x) == num for x in range(num//2, num+1))


