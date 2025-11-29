# Time:  O(n)
# Space: O(1)

# string, hash table
class Solution(object):
    def greatestLetter(self, s):
        """
        """
        lookup = set(s)
        result = ""
        for c in s:
            if c.isupper() and lower(c) in s:
                if c > result:
                    result = c
        return result


