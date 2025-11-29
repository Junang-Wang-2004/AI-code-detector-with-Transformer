# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def closestDivisors(self, num):
        """
        """
        def divisors(n):
            for d in reversed(range(1, int(n**0.5)+1)):
                if n % d == 0:
                    return d, n//d
            return 1, n

        return min([divisors(num+1), divisors(num+2)], key=lambda x: x[1]-x[0])



