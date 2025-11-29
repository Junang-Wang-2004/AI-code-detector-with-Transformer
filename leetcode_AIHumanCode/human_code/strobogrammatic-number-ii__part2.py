# Time:  O(n * 5^(n/2))
# Space: O(n)
class Solution2(object):
    def findStrobogrammatic(self, n):
        """
        """
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        def findStrobogrammaticRecu(n, k):
            if k == 0:
                return ['']
            elif k == 1:
                return ['0', '1', '8']
            result = []
            for num in findStrobogrammaticRecu(n, k - 2):
                for key, val in lookup.items():
                    if n != k or key != '0':
                        result.append(key + num + val)
            return result

        return findStrobogrammaticRecu(n, n)

