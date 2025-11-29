class Solution:
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        row_full, row_remainder = divmod(height, sideLength)
        col_full, col_remainder = divmod(width, sideLength)
        region_counts = [
            ((row_full + 1) * (col_full + 1), row_remainder * col_remainder),
            ((row_full + 1) * col_full, row_remainder * (sideLength - col_remainder)),
            (row_full * (col_full + 1), (sideLength - row_remainder) * col_remainder),
            (row_full * col_full, (sideLength - row_remainder) * (sideLength - col_remainder))
        ]
        region_counts.sort(key=lambda x: x[0], reverse=True)
        total_ones = 0
        remaining_capacity = maxOnes
        for multiplicity, region_size in region_counts:
            if remaining_capacity == 0:
                break
            ones_to_place = min(remaining_capacity, region_size)
            total_ones += ones_to_place * multiplicity
            remaining_capacity -= ones_to_place
        return total_ones
