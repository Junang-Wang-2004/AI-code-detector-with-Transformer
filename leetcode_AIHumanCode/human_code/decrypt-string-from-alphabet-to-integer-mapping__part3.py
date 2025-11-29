# Time:  O(n)
# Space: O(1)
import re


# regex solution
class Solution3(object):
    def freqAlphabets(self, s):
        """
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        return "".join(alpha(i[:2]) for i in re.findall(r"\d\d#|\d", s))
