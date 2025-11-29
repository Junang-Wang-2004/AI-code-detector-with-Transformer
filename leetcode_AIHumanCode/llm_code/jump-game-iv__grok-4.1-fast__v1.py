import collections
from collections import deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        idx_by_num = collections.defaultdict(list)
        for j, num in enumerate(arr):
            idx_by_num[num].append(j)
        visited_idxs = set([0])
        q = deque([(0, 0)])
        handled_nums = set()
        while q:
            idx, dist = q.popleft()
            if idx == n - 1:
                return dist
            for offset in [-1, 1]:
                adj_idx = idx + offset
                if 0 <= adj_idx < n and adj_idx not in visited_idxs:
                    visited_idxs.add(adj_idx)
                    q.append((adj_idx, dist + 1))
            num_here = arr[idx]
            if num_here not in handled_nums:
                handled_nums.add(num_here)
                for other_idx in idx_by_num[num_here]:
                    if other_idx not in visited_idxs:
                        visited_idxs.add(other_idx)
                        q.append((other_idx, dist + 1))
