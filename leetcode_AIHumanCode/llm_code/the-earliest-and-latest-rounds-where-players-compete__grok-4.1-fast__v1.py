from functools import lru_cache
from typing import Tuple, List
import sys

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def compute_bounds(total: int, dist_left: int, dist_right: int) -> Tuple[int, int]:
            if dist_left == dist_right:
                return 1, 1
            orig_left, orig_right = dist_left, dist_right
            if dist_left > dist_right:
                dist_left, dist_right = dist_right, dist_left
            min_round = sys.maxsize
            max_round = 0
            next_total = (total + 1) // 2
            num_matches = total // 2
            for split in range(dist_left + 1):
                adv_left = split + 1
                elim_left = dist_left - split
                low_right = max(elim_left, dist_right - (num_matches - elim_left))
                high_right = min(dist_right - adv_left, next_total - adv_left - 1)
                for pos_right in range(low_right, high_right + 1):
                    sub_min, sub_max = compute_bounds(next_total, split, pos_right)
                    min_round = min(min_round, sub_min + 1)
                    max_round = max(max_round, sub_max + 1)
            return min_round, max_round

        early, late = compute_bounds(n, firstPlayer - 1, n - secondPlayer)
        return [early, late]
