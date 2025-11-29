class Solution:
    def minimumCost(self, sentence, k):
        words = sentence.split()
        if not words:
            return 0
        word_lengths = [len(w) for w in words]
        n = len(word_lengths)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = float('inf')
            line_sum = 0
            for p in range(i - 1, -1, -1):
                line_sum += word_lengths[p]
                if p < i - 1:
                    line_sum += 1
                if line_sum > k:
                    break
                cost = (k - line_sum) ** 2
                dp[i] = min(dp[i], dp[p] + cost)
        ans = float('inf')
        line_sum = 0
        for p in range(n - 1, -1, -1):
            line_sum += word_lengths[p]
            if p < n - 1:
                line_sum += 1
            if line_sum > k:
                break
            ans = min(ans, dp[p])
        return int(ans)
