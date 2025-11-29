# Time:  O(n^4 * n!)
# Space: O(n * n!)

# bfs
class Solution(object):
    def minSplitMerge(self, nums1, nums2):
        """
        """
        def bfs(start, target):
            def adj(arr):
                for l in range(len(arr)):
                    for r in range(l, len(arr)):
                        sub = arr[l:r+1]
                        rem = arr[:l]+arr[r+1:]
                        for i in range(len(rem)+1):
                            if i == l:
                                continue
                            yield rem[:i]+sub+rem[i:]

            d = 0
            if start == target:
                return d
            lookup = {start}
            q = [start]
            d += 1
            while q:
                new_q = []
                for u in q:
                    for v in adj(u):
                        if v in lookup:
                            continue
                        if v == target:
                            return d
                        lookup.add(v)
                        new_q.append(v)
                q = new_q
                d += 1
            return -1
    
        return bfs(tuple(nums1), tuple(nums2))


