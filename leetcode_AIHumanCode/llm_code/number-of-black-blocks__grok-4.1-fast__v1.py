from collections import defaultdict
from typing import List

class Solution:
    def countBlackBlocks(self, h: int, w: int, points: List[List[int]]) -> List[int]:
        block_cnt = defaultdict(int)
        for r, c in points:
            for dr in range(-1, 1):
                br = r + dr
                if 0 <= br < h - 1:
                    for dc in range(-1, 1):
                        bc = c + dc
                        if 0 <= bc < w - 1:
                            block_cnt[(br, bc)] += 1
        ans = [0] * 5
        for k in block_cnt.values():
            ans[k] += 1
        total = (h - 1) * (w - 1)
        ans[0] = total - sum(ans[1:])
        return ans
