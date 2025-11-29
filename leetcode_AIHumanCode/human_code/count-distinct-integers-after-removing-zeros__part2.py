# Time:  O(logn)
# Space: O(logn)
# combinatorics
class Solution2(object):
    def countDistinct(self, n):
        """
        """
        s = str(n)
        base = pow(9, len(s))
        result = (base-9)//(9-1)
        base //= 9
        for x in s:
            if x == '0':
                break
            result += ((ord(x)-ord('0'))-1)*base
            base //= 9
        if base == 0:
            result += 1
        return result
