# Time:  O(10^(l/2) * n), l = 5
# Space: O(10^(l/2) * n)

# freq table, prefix sum
class Solution(object):
    def countPalindromes(self, s):
        """
        """
        MOD = 10**9+7
        cnt = [0]*10
        left = [[[0]*10 for _ in range(10)] for _ in range(len(s)+1)]
        for k in range(len(s)):
            left[k+1] = [[left[k][i][j] for j in range(10)] for i in range(10)]
            for i in range(10):
                left[k+1][int(s[k])][i] += cnt[i]
            cnt[int(s[k])] += 1
        cnt = [0]*10
        right = [[0]*10 for _ in range(10)]
        result = 0
        for k in reversed(range(len(s))):
            for i in range(10):
                for j in range(10):
                    result = (result+left[k][i][j]*right[i][j])%MOD
            for i in range(10):
                right[int(s[k])][i] += cnt[i]
            cnt[int(s[k])] += 1
        return result
                    

