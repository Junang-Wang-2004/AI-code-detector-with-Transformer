class Solution(object):
    def sampleStats(self, count):
        length = len(count)
        overall = sum(count)
        low = 0
        while count[low] == 0:
            low += 1
        high = length - 1
        while count[high] == 0:
            high -= 1
        weighted = 0
        for idx in range(length):
            weighted += idx * count[idx]
        avg = weighted / overall
        peak_count = -1
        peak_val = 0
        for idx in range(length):
            if count[idx] > peak_count:
                peak_count = count[idx]
                peak_val = idx
        target1 = (overall + 1) // 2
        accum1 = 0
        for idx in range(length):
            accum1 += count[idx]
            if accum1 >= target1:
                mid1 = idx
                break
        target2 = (overall + 2) // 2
        accum2 = 0
        for idx in range(length):
            accum2 += count[idx]
            if accum2 >= target2:
                mid2 = idx
                break
        mid_val = (mid1 + mid2) / 2
        return [float(low), float(high), avg, mid_val, float(peak_val)]
