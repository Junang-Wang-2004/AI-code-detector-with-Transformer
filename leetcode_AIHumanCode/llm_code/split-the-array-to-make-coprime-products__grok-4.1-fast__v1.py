class Solution(object):
    def findValidSplit(self, nums):
        def get_factors(val):
            facs = []
            d = 2
            while d * d <= val:
                exp = 0
                while val % d == 0:
                    val //= d
                    exp += 1
                if exp > 0:
                    facs.append((d, exp))
                d += 1 if d == 2 else 2
            if val > 1:
                facs.append((val, 1))
            return facs
        
        n = len(nums)
        last_occurrence = {}
        for idx in range(n - 1, -1, -1):
            for prime, _ in get_factors(nums[idx]):
                if prime not in last_occurrence:
                    last_occurrence[prime] = idx
        
        farthest = -1
        for pos in range(n - 1):
            for prime, _ in get_factors(nums[pos]):
                if prime in last_occurrence:
                    farthest = max(farthest, last_occurrence[prime])
            if farthest <= pos:
                return pos
        return -1
