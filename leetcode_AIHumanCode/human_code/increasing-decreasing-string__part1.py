# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortString(self, s):
        """
        """
        result, count = [], [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        while len(result) != len(s):
            for c in range(len(count)):
                if not count[c]:
                    continue
                result.append(chr(ord('a')+c))
                count[c] -= 1
            for c in reversed(range(len(count))):
                if not count[c]:
                    continue
                result.append(chr(ord('a')+c))
                count[c] -= 1
        return "".join(result)


