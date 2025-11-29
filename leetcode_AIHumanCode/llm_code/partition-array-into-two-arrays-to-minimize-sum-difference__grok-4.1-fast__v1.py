import bisect

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)
        h = n // 2
        a = nums[:h]
        b = nums[h:]

        def get_sums(arr):
            sz = len(arr)
            res = [[] for _ in range(sz + 1)]
            def search(i, sm, ct):
                if i == sz:
                    res[ct].append(sm)
                    return
                search(i + 1, sm, ct)
                search(i + 1, sm + arr[i], ct + 1)
            search(0, 0, 0)
            for c in range(sz + 1):
                res[c].sort()
            return res

        sums_a = get_sums(a)
        sums_b = get_sums(b)
        tot = sum(nums)
        mind = float('inf')
        for x in range(h + 1):
            y = h - x
            lista = sums_a[x]
            listb = sums_b[y]
            for sa in lista:
                goal = tot / 2 - sa
                p = bisect.bisect_left(listb, goal)
                for q in (p - 1, p):
                    if 0 <= q < len(listb):
                        sb = listb[q]
                        d = abs(2 * (sa + sb) - tot)
                        if d < mind:
                            mind = d
        return mind
