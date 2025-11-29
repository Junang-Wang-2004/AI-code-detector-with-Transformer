class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        res = []
        vis = [False] * 26
        for ch in s:
            i = ord(ch) - ord('a')
            freq[i] -= 1
            if not vis[i]:
                while res and ord(res[-1]) > ord(ch) and freq[ord(res[-1]) - ord('a')] > 0:
                    vis[ord(res.pop()) - ord('a')] = False
                res.append(ch)
                vis[i] = True
        return ''.join(res)
