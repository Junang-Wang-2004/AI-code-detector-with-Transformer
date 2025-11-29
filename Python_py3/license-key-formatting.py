# Time:  O(n)
# Space: O(1)

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        """
        result = []
        for i in reversed(range(len(S))):
            if S[i] == '-':
                continue
            if len(result) % (K + 1) == K:
                result += '-'
            result += S[i].upper()
        return "".join(reversed(result))
