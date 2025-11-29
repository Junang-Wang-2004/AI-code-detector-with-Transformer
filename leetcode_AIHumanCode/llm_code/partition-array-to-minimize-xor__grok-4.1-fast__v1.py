class Solution:
    def minXor(self, nums, k):
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]
        
        def feasible(target):
            cuts = 0
            cur = 0
            while cur < n:
                cuts += 1
                if cuts > k:
                    return False
                xor_base = pref[cur]
                nxt = cur
                while nxt < n and (pref[nxt + 1] ^ xor_base) <= target:
                    nxt += 1
                if nxt == cur:
                    return False
                cur = nxt
            return True
        
        low = 0
        high = (1 << 31) - 1
        while low < high:
            m = (low + high) // 2
            if feasible(m):
                high = m
            else:
                low = m + 1
        return low
