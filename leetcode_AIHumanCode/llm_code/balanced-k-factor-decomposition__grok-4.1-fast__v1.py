import bisect

class Solution:
    def minDifference(self, n, k):
        self.best_path = []
        self.min_range = float('inf')

        def get_divisors(val):
            divisors = []
            i = 1
            while i * i <= val:
                if val % i == 0:
                    divisors.append(i)
                    if i != val // i:
                        divisors.append(val // i)
                i += 1
            divisors.sort()
            return divisors

        def search(prod_left, parts, lower_bound, path):
            if parts == k:
                if prod_left == 1:
                    rng = path[-1] - path[0]
                    if rng < self.min_range:
                        self.min_range = rng
                        self.best_path = path[:]
                return
            if path and path[-1] - path[0] >= self.min_range:
                return
            divisors = get_divisors(prod_left)
            start_idx = bisect.bisect_left(divisors, lower_bound)
            for j in range(len(divisors) - 1, start_idx - 1, -1):
                factor = divisors[j]
                path.append(factor)
                search(prod_left // factor, parts + 1, factor, path)
                path.pop()

        search(n, 0, 1, [])
        return self.best_path
