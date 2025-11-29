from functools import reduce
# Time:  O(blogb)
# Space: O(1)
# brute force, hash table, bitmasks
class Solution3(object):
    def numberCount(self, a, b):
        """
        """
        def check(x):
            lookup = 0
            while x:
                if lookup&(1<<(x%10)):
                    return False
                lookup |= (1<<(x%10))
                x //= 10
            return True

        return sum(check(x) for x in range(a, b+1))


