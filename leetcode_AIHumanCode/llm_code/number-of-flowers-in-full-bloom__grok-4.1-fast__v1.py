class Solution:
    def fullBloomFlowers(self, flowers, persons):
        starts = sorted(start for start, end in flowers)
        finishes = sorted(end + 1 for start, end in flowers)
        timed_queries = sorted(enumerate(persons), key=lambda p: p[1])
        result = [0] * len(persons)
        start_idx = 0
        finish_idx = 0
        for orig_idx, arrival in timed_queries:
            while start_idx < len(starts) and starts[start_idx] <= arrival:
                start_idx += 1
            while finish_idx < len(finishes) and finishes[finish_idx] <= arrival:
                finish_idx += 1
            result[orig_idx] = start_idx - finish_idx
        return result
