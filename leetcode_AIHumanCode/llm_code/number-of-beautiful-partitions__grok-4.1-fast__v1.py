class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        starts_prime = [False] * n
        ends_prime = set('2357')
        for i in range(n):
            starts_prime[i] = s[i] in ends_prime
        ways = [[0] * (k + 1) for _ in range(n + 1)]
        ways[0][0] = 1
        for num_parts in range(1, k + 1):
            prefix_sum = 0
            for end_len in range(1, n + 1):
                start_idx = end_len - minLength
                if start_idx >= 0 and starts_prime[start_idx]:
                    prefix_sum = (prefix_sum + ways[start_idx][num_parts - 1]) % MOD
                if s[end_len - 1] not in ends_prime:
                    ways[end_len][num_parts] = prefix_sum
        return ways[n][k]
