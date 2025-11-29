# Time:  O(sqrt(n))
# Space: O(sqrt(n))
class Solution2(object):
    def kthFactor(self, n, k):
        """
        """
        result = []
        i = 1
        while i*i <= n:
            if not n%i:
                if i*i != n:
                    result.append(i)
                k -= 1
                if not k:
                    return i
            i += 1
        return -1 if k > len(result) else n//result[-k]
