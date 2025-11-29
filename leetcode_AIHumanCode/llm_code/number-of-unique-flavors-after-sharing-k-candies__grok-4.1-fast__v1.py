class Solution(object):
    def shareCandies(self, candies, k):
        n = len(candies)
        freq = {}
        for i in range(k, n):
            t = candies[i]
            freq[t] = freq.get(t, 0) + 1
        ans = len(freq)
        remove_idx = k
        for insert_idx in range(n - k):
            rem_type = candies[remove_idx]
            freq[rem_type] -= 1
            if freq[rem_type] == 0:
                del freq[rem_type]
            ins_type = candies[insert_idx]
            if ins_type in freq:
                freq[ins_type] += 1
            else:
                freq[ins_type] = 1
            ans = max(ans, len(freq))
            remove_idx += 1
        return ans
