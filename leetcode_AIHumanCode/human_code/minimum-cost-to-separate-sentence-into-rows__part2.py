# Time:  O(s + n * k), n is the number of the word_lens
# Space: O(n)
class Solution2(object):
    def minimumCost(self, sentence, k):
        """
        """
        word_lens = []
        j = 0
        for i in range(len(sentence)+1):
            if i != len(sentence) and sentence[i] != ' ':
                continue
            word_lens.append(i-j)
            j = i+1
        dp = [float("inf")]*(len(word_lens))  # dp[i]: min cost of word_lens[i:]
        i, total = len(word_lens)-1, -1
        while i >= 0 and total + (word_lens[i]+1) <= k:  # find max i s.t. the length of the last line > k
            total += (word_lens[i]+1)
            dp[i] = 0
            i -= 1
        for i in reversed(range(i+1)):
            total = word_lens[i]
            for j in range(i+1, len(dp)):
                dp[i] = min(dp[i], dp[j] + (k-total)**2)
                total += (word_lens[j]+1)
                if total > k:
                    break
        return dp[0]


