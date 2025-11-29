# Time:  O(n * 5^(n/2))
# Space: O(n)

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        """
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        result = ['0', '1', '8'] if n%2 else ['']
        for i in range(n%2, n, 2):
            result = [a + num + b for a, b in lookup.items() if i != n-2 or a != '0' for num in result]
        return result


