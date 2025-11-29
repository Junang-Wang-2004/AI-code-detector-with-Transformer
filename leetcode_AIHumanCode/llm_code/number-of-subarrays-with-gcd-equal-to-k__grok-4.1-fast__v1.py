class Solution(object):
    def subarrayGCD(self, nums, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ans = 0
        states = {}
        for num in nums:
            if num % k != 0:
                states = {}
                continue
            fresh = {num: 1}
            for prev_d, ways in states.items():
                nd = gcd(prev_d, num)
                fresh[nd] = fresh.get(nd, 0) + ways
            states = fresh
            ans += states.get(k, 0)
        return ans
