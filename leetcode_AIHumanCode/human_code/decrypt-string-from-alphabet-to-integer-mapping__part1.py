# Time:  O(n)
# Space: O(1)

# forward solution
class Solution(object):
    def freqAlphabets(self, s):
        """
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = 0
        result = []
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                result.append(alpha(s[i:i+2]))
                i += 3
            else:
                result.append(alpha(s[i]))
                i += 1
        return "".join(result)


