from sortedcontainers import SortedList
import collections

class Solution(object):
    def findXSum(self, nums, k, x):
        freq = collections.Counter()
        sl = SortedList()
        cur = 0
        ans = []
        l = 0
        def add_upd(v):
            nonlocal cur
            e = (-freq[v], -v)
            sl.add(e)
            i = sl.index(e)
            if i < x:
                cur += freq[v] * v
                if x < len(sl):
                    nc, nv = sl[x]
                    cur -= nc * nv
        def rem_upd(v):
            nonlocal cur
            e = (-freq[v], -v)
            i = sl.index(e)
            if i < x:
                cur -= freq[v] * v
                if x < len(sl):
                    nc, nv = sl[x]
                    cur += nc * nv
            sl.remove(e)
        for r in range(len(nums)):
            v = nums[r]
            if freq[v] > 0:
                rem_upd(v)
            freq[v] += 1
            add_upd(v)
            if r >= k - 1:
                ans.append(cur)
                ov = nums[l]
                rem_upd(ov)
                freq[ov] -= 1
                if freq[ov] > 0:
                    add_upd(ov)
                else:
                    del freq[ov]
                l += 1
        return ans
