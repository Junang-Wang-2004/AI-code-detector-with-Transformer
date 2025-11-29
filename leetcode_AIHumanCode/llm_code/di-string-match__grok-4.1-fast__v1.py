class Solution:
    def diStringMatch(self, S):
        n = len(S)
        ans = [0] * (n + 1)
        mn, mx = 0, n
        for i in range(n):
            if S[i] == 'I':
                ans[i] = mn
                mn += 1
            else:
                ans[i] = mx
                mx -= 1
        ans[n] = mn
        return ans
