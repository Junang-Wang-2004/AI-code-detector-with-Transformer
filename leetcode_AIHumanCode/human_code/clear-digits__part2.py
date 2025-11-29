# Time:  O(n)
# Space: O(1)
# stack
class Solution2(object):
    def clearDigits(self, s):
        """
        """
        result = []
        for x in s:
            if x.isdigit():
                result.pop()
                continue
            result.append(x)
        return "".join(result)
