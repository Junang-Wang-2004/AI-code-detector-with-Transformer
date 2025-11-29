from collections import deque

class Solution:
    def kEmptySlots(self, flowers, k):
        n = len(flowers)
        bloom_day = [0] * n
        for day, pos in enumerate(flowers):
            bloom_day[pos - 1] = day
        window_size = k
        min_in_window = [float('inf')] * (n - window_size + 1)
        monotonic_queue = deque()
        for idx in range(n):
            while monotonic_queue and bloom_day[monotonic_queue[-1]] >= bloom_day[idx]:
                monotonic_queue.pop()
            monotonic_queue.append(idx)
            if monotonic_queue[0] == idx - window_size:
                monotonic_queue.popleft()
            if idx >= window_size - 1:
                min_in_window[idx - window_size + 1] = bloom_day[monotonic_queue[0]]
        earliest = float('inf')
        for left_pos in range(n - k - 1):
            right_pos = left_pos + k + 1
            candidate_day = max(bloom_day[left_pos], bloom_day[right_pos])
            gap_min = min_in_window[left_pos + 1]
            if gap_min > candidate_day:
                earliest = min(earliest, candidate_day)
        return earliest + 1 if earliest < float('inf') else -1
