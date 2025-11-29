class Solution:
    def maximumPopulation(self, logs):
        earliest = 1950
        latest = 2050
        peak_count = -1
        peak_year = earliest
        for y in range(earliest, latest + 1):
            alive = sum(b <= y < d for b, d in logs)
            if alive > peak_count:
                peak_count = alive
                peak_year = y
        return peak_year
