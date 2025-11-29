# Time:  O(n * l)
# Space: O(1)

# math
class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        """
        def reverse(x):
            result = 0
            while x:
                result = result*10+x%10
                x //= 10
            return result

        def f(l, x):
            x = 10**((l-1)//2)+(x-1)
            if x > 10**((l+1)//2)-1:
                return -1
            return x*10**(l//2)+reverse(x//10 if l%2 else x)

        return [f(intLength, x) for x in queries]


