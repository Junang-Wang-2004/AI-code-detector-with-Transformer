class Solution(object):
    def findPrimePairs(self, n):
        if n < 4:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        pairs = []
        for i in range(2, n // 2 + 1):
            if is_prime[i] and is_prime[n - i]:
                pairs.append([i, n - i])
        return pairs
