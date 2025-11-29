import collections

class Solution(object):
    def countPairs(self, coordinates, k):
        freq = collections.Counter(tuple(p) for p in coordinates)
        total = 0
        for curr in freq:
            cx, cy = curr
            for split in range(k + 1):
                px = cx ^ split
                py = cy ^ (k - split)
                prev = (px, py)
                if prev < curr:
                    continue
                count_curr = freq[curr]
                count_prev = freq[prev]
                if prev == curr:
                    total += count_curr * (count_curr - 1) // 2
                else:
                    total += count_curr * count_prev
        return total
