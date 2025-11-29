import collections

class Solution(object):
    def primeSubarray(self, nums, k):
        MAX = 50000
        is_prime = [True] * (MAX + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX + 1, i):
                    is_prime[j] = False
        pos = [i for i, v in enumerate(nums) if v <= MAX and is_prime[v]]
        npos = len(pos)
        if npos < 2:
            return 0
        val = [nums[pos[i]] for i in range(npos)]
        qmax = collections.deque()
        qmin = collections.deque()
        ans = 0
        plef = 0
        for j in range(npos):
            while qmax and val[qmax[-1]] <= val[j]:
                qmax.pop()
            qmax.append(j)
            while qmin and val[qmin[-1]] >= val[j]:
                qmin.pop()
            qmin.append(j)
            while val[qmax[0]] - val[qmin[0]] > k:
                if qmax and qmax[0] == plef:
                    qmax.popleft()
                if qmin and qmin[0] == plef:
                    qmin.popleft()
                plef += 1
            if j - plef + 1 >= 2:
                pprev = pos[j - 1]
                st = 0 if plef == 0 else pos[plef - 1] + 1
                ans += pprev - st + 1
        return ans
