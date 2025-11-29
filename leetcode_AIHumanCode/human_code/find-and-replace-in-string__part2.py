# Time:  O(mlogm + m * n)
# Space: O(n + m)
class Solution2(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        """
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i+len(s)] == s:
                S = S[:i] + t + S[i+len(s):]

        return S
