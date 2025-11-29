# Time:  O(n^4 * n!)
# Space: O(n * n!)
# bfs
class Solution2(object):
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
            lookup = {start}
            q = [start]
            while q:
                new_q = []
                for u in q:
                    if u == target:
                        return d
                    for v in adj(u):
                        if v in lookup:
                            continue
                        lookup.add(v)
                        new_q.append(v)
                q = new_q
                d += 1
            return -1

        return bfs(tuple(nums1), tuple(nums2))
