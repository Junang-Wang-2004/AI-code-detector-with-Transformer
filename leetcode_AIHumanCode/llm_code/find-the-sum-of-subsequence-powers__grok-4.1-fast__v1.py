class Solution(object):
    def sumOfPowers(self, nums, k):
        MOD = 10**9 + 7
        a = sorted(nums)
        n = len(a)
        possible_mins = sorted(set(a[j] - a[i] for i in range(n) for j in range(i + 1, n)), reverse=True)
        answer = 0
        last_count = 0
        for threshold in possible_mins:
            ways = [[0] * (k + 1) for _ in range(n + 1)]
            ways[0][0] = 1
            ptr = 0
            for idx in range(n):
                while ptr < n and a[idx] - a[ptr] >= threshold:
                    ptr += 1
                for sz in range(1, k + 1):
                    ways[idx + 1][sz] = (ways[idx + 1][sz] + ways[ptr][sz - 1]) % MOD
                for sz in range(k + 1):
                    ways[idx + 1][sz] = (ways[idx + 1][sz] + ways[idx][sz]) % MOD
            current_count = ways[n][k]
            increment = (current_count - last_count + MOD) % MOD
            answer = (answer + threshold * increment) % MOD
            last_count = current_count
        return answer
