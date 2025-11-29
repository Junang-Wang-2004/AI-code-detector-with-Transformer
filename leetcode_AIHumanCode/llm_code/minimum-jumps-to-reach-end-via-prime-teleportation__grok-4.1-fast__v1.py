import collections

def smallest_prime_factors(limit):
    spf = list(range(limit + 1))
    spf[0] = spf[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

MAXN = 10**6
SPF = smallest_prime_factors(MAXN)

class Solution(object):
    def minJumps(self, nums):
        n = len(nums)
        div_by_prime = collections.defaultdict(list)
        for idx, value in enumerate(nums):
            temp = value
            while temp > 1:
                pf = SPF[temp]
                while temp % pf == 0:
                    temp //= pf
                div_by_prime[pf].append(idx)
        dist_arr = [-1] * n
        dist_arr[0] = 0
        q = collections.deque([0])
        handled_primes = set()
        while q:
            current = q.popleft()
            if current == n - 1:
                return dist_arr[n - 1]
            for step in (-1, 1):
                neighbor = current + step
                if 0 <= neighbor < n and dist_arr[neighbor] == -1:
                    dist_arr[neighbor] = dist_arr[current] + 1
                    q.append(neighbor)
            prime_val = nums[current]
            if prime_val > 1 and SPF[prime_val] == prime_val and prime_val not in handled_primes:
                handled_primes.add(prime_val)
                for dest in div_by_prime[prime_val]:
                    if dist_arr[dest] == -1:
                        dist_arr[dest] = dist_arr[current] + 1
                        q.append(dest)
        return dist_arr[n - 1]
