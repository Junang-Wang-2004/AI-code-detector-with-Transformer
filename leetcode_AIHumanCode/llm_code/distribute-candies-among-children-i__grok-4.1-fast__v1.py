class Solution:
    def distributeCandies(self, n, limit):
        def count_ways(total):
            if total < 0:
                return 0
            return (total + 2) * (total + 1) // 2
        
        max_per_child = limit + 1
        result = count_ways(n)
        result -= 3 * count_ways(n - max_per_child)
        result += 3 * count_ways(n - 2 * max_per_child)
        result -= count_ways(n - 3 * max_per_child)
        return result
