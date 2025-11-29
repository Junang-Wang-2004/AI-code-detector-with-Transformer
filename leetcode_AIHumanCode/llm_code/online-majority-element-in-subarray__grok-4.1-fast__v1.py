import collections
import random
import bisect

class MajorityChecker:
    def __init__(self, nums):
        self.values = nums
        self.indices = collections.defaultdict(list)
        for pos, val in enumerate(nums):
            self.indices[val].append(pos)
        self.sample_count = 35

    def query(self, start, end, min_count):
        for attempt in range(self.sample_count):
            selected_pos = random.randint(start, end)
            candidate_val = self.values[selected_pos]
            pos_list = self.indices[candidate_val]
            occurrences = bisect.bisect_right(pos_list, end) - bisect.bisect_left(pos_list, start)
            if occurrences >= min_count:
                return candidate_val
        return -1
